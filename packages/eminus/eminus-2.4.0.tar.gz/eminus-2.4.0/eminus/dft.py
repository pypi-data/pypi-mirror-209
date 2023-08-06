#!/usr/bin/env python3
'''Main DFT functions based on the DFT++ formulation.'''
import numpy as np
from numpy.random import Generator, SFC64
from scipy.linalg import eig, eigh, eigvalsh, inv, norm, sqrtm

from .gth import calc_Vnonloc
from .utils import handle_spin_gracefully, pseudo_uniform
from .xc import get_vxc


def solve_poisson(atoms, n):
    '''Solve the Poisson equation.

    Reference: Comput. Phys. Commun. 128, 1.

    Args:
        atoms: Atoms object.
        n (ndarray): Real-space electronic density.

    Returns:
        ndarray: Hartree field.
    '''
    # phi = -4 pi Linv(O(J(n)))
    return -4 * np.pi * atoms.Linv(atoms.O(atoms.J(n)))


def get_n_total(atoms, Y, n_spin=None):
    '''Calculate the total electronic density.

    Reference: Comput. Phys. Commun. 128, 1.

    Args:
        atoms: Atoms object.
        Y (ndarray): Expansion coefficients of orthogonal wave functions in reciprocal space.

    Keyword Args:
        n_spin (ndarray): Real-space electronic densities per spin channel.

    Returns:
        ndarray: Electronic density.
    '''
    # Return the total density in the spin-paired case
    if n_spin is not None:
        return np.sum(n_spin, axis=0)

    # n = (IW) F (IW)dag
    Yrs = atoms.I(Y)
    n = np.zeros(len(atoms.r))
    for spin in range(atoms.Nspin):
        n += np.sum(atoms.f[spin] * np.real(Yrs[spin].conj() * Yrs[spin]), axis=1)
    return n


def get_n_spin(atoms, Y, n=None):
    '''Calculate the electronic density per spin channel.

    Reference: Comput. Phys. Commun. 128, 1.

    Args:
        atoms: Atoms object.
        Y (ndarray): Expansion coefficients of orthogonal wave functions in reciprocal space.

    Keyword Args:
        n (ndarray): Real-space electronic density.

    Returns:
        ndarray: Electronic densities per spin channel.
    '''
    # Return the total density in the spin-paired case
    if n is not None and atoms.Nspin == 1:
        return np.atleast_2d(n)

    Yrs = atoms.I(Y)
    n = np.empty((atoms.Nspin, len(atoms.r)))
    for spin in range(atoms.Nspin):
        n[spin] = np.sum(atoms.f[spin] * np.real(Yrs[spin].conj() * Yrs[spin]), axis=1)
    return n


def get_n_single(atoms, Y):
    '''Calculate the single-electron densities.

    Args:
        atoms: Atoms object.
        Y (ndarray): Expansion coefficients of orthogonal wave functions in reciprocal space.

    Returns:
        ndarray: Single-electron densities.
    '''
    Yrs = atoms.I(Y)
    n = np.empty((atoms.Nspin, len(atoms.r), atoms.Nstate))
    for spin in range(atoms.Nspin):
        n[spin] = atoms.f[spin] * np.real(Yrs[spin].conj() * Yrs[spin])
    return n


def get_grad_n_spin(atoms, n_spin):
    '''Calculate the gradient of densities per spin channel.

    Args:
        atoms: Atoms object.
        n_spin (ndarray): Real-space electronic densities per spin channel.

    Returns:
        ndarray: Gradients of densities per spin channel.
    '''
    dn_spin = np.empty((atoms.Nspin, len(atoms.r), 3))
    for spin in range(atoms.Nspin):
        Gn = 1j * atoms.G * atoms.J(n_spin[spin])[:, None]
        for i in range(3):
            dn_spin[spin, :, i] = np.real(atoms.I(Gn[:, i]))
    return dn_spin


@handle_spin_gracefully
def orth(atoms, W):
    '''Orthogonalize coefficient matrix W.

    Reference: Comput. Phys. Commun. 128, 1.

    Args:
        atoms: Atoms object.
        W (ndarray): Expansion coefficients of unconstrained wave functions in reciprocal space.

    Returns:
        ndarray: Orthogonalized wave functions.
    '''
    # Y = W (Wdag O(W))^-0.5
    return W @ inv(sqrtm(W.conj().T @ atoms.O(W)))


def get_grad(scf, spin, W, *args, **kwargs):
    '''Calculate the energy gradient with respect to W.

    Reference: Comput. Phys. Commun. 128, 1.

    Args:
        scf: SCF object.
        spin (int): Spin variable to track weather to calculate the gradient for spin up or down.
        W (ndarray): Expansion coefficients of unconstrained wave functions in reciprocal space.

    Returns:
        ndarray: Gradient.
    '''
    atoms = scf.atoms
    F = np.diag(atoms.f[spin])
    HW = H(scf, spin, W, *args, **kwargs)
    WHW = W[spin].conj().T @ HW
    # U = Wdag O(W)
    OW = atoms.O(W[spin])
    U = W[spin].conj().T @ OW
    invU = inv(U)
    U12 = sqrtm(invU)
    # Htilde = U^-0.5 Wdag H(W) U^-0.5
    Ht = U12 @ WHW @ U12
    # grad E = H(W) - O(W) U^-1 (Wdag H(W)) (U^-0.5 F U^-0.5) + O(W) (U^-0.5 Q(Htilde F - F Htilde))
    return (HW - (OW @ invU) @ WHW) @ (U12 @ F @ U12) + OW @ (U12 @ Q(Ht @ F - F @ Ht, U))


def H(scf, spin, W, Y=None, n=None, n_spin=None, dn_spin=None, phi=None, vxc=None, vsigma=None):
    '''Left-hand side of the eigenvalue equation.

    Reference: Comput. Phys. Commun. 128, 1.

    Args:
        scf: SCF object.
        spin (int): Spin variable to track weather to calculate the gradient for spin up or down.
        W (ndarray): Expansion coefficients of unconstrained wave functions in reciprocal space.

    Keyword Args:
        Y (ndarray): Expansion coefficients of orthogonal wave functions in reciprocal space.
        n (ndarray): Real-space electronic density.
        n_spin (ndarray): Real-space electronic densities per spin channel.
        dn_spin (ndarray): Real-space gradient of densities per spin channel.
        phi (ndarray): Hartree field.
        vxc (ndarray): Exchange-correlation potential.
        vsigma (ndarray): Contracted gradient potential derivative.

    Returns:
        ndarray: Hamiltonian applied on W.
    '''
    atoms = scf.atoms
    # One can calculate everything from W,
    # but one can also use already computed results to save time
    if Y is None:
        Y = orth(atoms, W)
    if n_spin is None:
        n_spin = get_n_spin(atoms, Y, n)
    if dn_spin is None and scf.psp == 'pbe':
        dn_spin = get_grad_n_spin(atoms, n_spin)
    if n is None:
        n = get_n_total(atoms, Y, n_spin)
    if phi is None:
        phi = solve_poisson(atoms, n)
    if vxc is None or (vsigma is None and scf.psp == 'pbe'):
        vxc, vsigma = get_vxc(scf.xc, n_spin, atoms.Nspin, dn_spin)

    # We get the full potential in the functional definition (different to the DFT++ notation)
    # Applay the gradient correction to the potential if a GGA functional is used
    if scf.psp == 'pbe':
        vxc = gradient_correction(atoms, dn_spin, vxc, vsigma)
    # Normally Vxc = Jdag(O(J(exc))) + diag(exc') Jdag(O(J(n)))
    Vxc = atoms.Jdag(atoms.O(atoms.J(vxc[spin])))
    # Vkin = -0.5 L(W)
    Vkin_psi = -0.5 * atoms.L(W[spin])
    # Veff = Jdag(Vion) + Jdag(O(J(vxc))) + Jdag(O(phi))
    Veff = scf.Vloc + Vxc + atoms.Jdag(atoms.O(phi))
    Vnonloc_psi = calc_Vnonloc(scf, W[spin])
    # H = Vkin + Idag(diag(Veff))I + Vnonloc
    # Diag(a) * B can be written as a * B if a is a column vector
    return Vkin_psi + atoms.Idag(Veff[:, None] * atoms.I(W[spin])) + Vnonloc_psi


def gradient_correction(atoms, dn_spin, vxc, vsigma):
    '''Calculate the gradient corrected exchange-correlation potential.

    Reference: Chem. Phys. Lett. 199, 557.

    Args:
        atoms: Atoms object.
        dn_spin (ndarray): Real-space gradient of densities per spin channel.
        vxc (ndarray): Exchange-correlation potential.
        vsigma (ndarray): Contracted gradient potential derivative.

    Returns:
        ndarray: Gradient corrected potential.
    '''
    # sigma is |dn|^2, while vsigma is n * d exc/d sigma
    h = np.zeros_like(dn_spin)
    if atoms.Nspin == 1:
        # In the unpolarized case we have no spin mixing and only one spin density
        h[0] = 2 * vsigma[0][:, None] * dn_spin[0]
    else:
        # In the polarized case we would get for spin up (and similar for spin down)
        # Vxc_u = vxc_u - Nabla dot (2 vsigma_uu * dn_u + vsigma_ud * dn_d)
        # h is the expression in the brackets
        h[0] = 2 * vsigma[0][:, None] * dn_spin[0] + vsigma[1][:, None] * dn_spin[1]
        h[1] = 2 * vsigma[2][:, None] * dn_spin[1] + vsigma[1][:, None] * dn_spin[0]

    # Calculate Nabla dot h
    divh = np.zeros_like(vxc)
    for spin in range(atoms.Nspin):
        Gh = np.empty((len(atoms.G2), 3), dtype=complex)
        for i in range(3):
            Gh[:, i] = atoms.J(h[spin, :, i])
        Gdivh = 1j * np.sum(atoms.G * Gh, axis=1)
        divh[spin] = np.real(atoms.I(Gdivh))

    # Subtract the gradient correction
    return vxc - divh


def Q(inp, U):
    '''Operator needed to calculate gradients with non-constant occupations.

    Reference: Comput. Phys. Commun. 128, 1.

    Args:
        inp (ndarray): Coefficients input array.
        U (ndarray): Overlap of wave functions.

    Returns:
        ndarray: Q operator result.
    '''
    mu, V = eig(U)
    mu = mu[:, None]
    denom = np.sqrt(mu) @ np.ones((1, len(mu)))
    denom2 = denom + denom.conj().T
    return V @ ((V.conj().T @ inp @ V) / denom2) @ V.conj().T


def get_psi(scf, W, n=None):
    '''Calculate eigenstates from H.

    Reference: Comput. Phys. Commun. 128, 1.

    Args:
        scf: SCF object.
        W (ndarray): Expansion coefficients of unconstrained wave functions in reciprocal space.

    Keyword Args:
        n (ndarray): Real-space electronic density.

    Returns:
        ndarray: Eigenstates in reciprocal space.
    '''
    atoms = scf.atoms
    Y = orth(atoms, W)
    psi = np.empty_like(Y)
    for spin in range(atoms.Nspin):
        mu = Y[spin].conj().T @ H(scf, spin, W=Y, n=n)
        _, D = eigh(mu)
        psi[spin] = Y[spin] @ D
    return psi


def get_epsilon(scf, W, n=None):
    '''Calculate eigenvalues from H.

    Reference: Comput. Phys. Commun. 128, 1.

    Args:
        scf: SCF object.
        W (ndarray): Expansion coefficients of unconstrained wave functions in reciprocal space.

    Keyword Args:
        n (ndarray): Real-space electronic density.

    Returns:
        ndarray: Eigenvalues.
    '''
    atoms = scf.atoms
    Y = orth(atoms, W)
    epsilon = np.empty((atoms.Nspin, atoms.Nstate))
    for spin in range(atoms.Nspin):
        mu = Y[spin].conj().T @ H(scf, spin, W=Y, n=n)
        epsilon[spin] = np.sort(eigvalsh(mu))
    return epsilon


def guess_random(scf, complex=True):
    '''Generate random initial-guess coefficients as starting values.

    Args:
        scf: SCF object.

    Keyword Args:
        complex (bool): Use complex numbers for the random guess.

    Returns:
        ndarray: Initial-guess orthogonal wave functions in reciprocal space.
    '''
    atoms = scf.atoms

    seed = 42
    rng = Generator(SFC64(seed))
    if complex:
        W = rng.standard_normal((atoms.Nspin, len(atoms.G2c), atoms.Nstate)) + \
            1j * rng.standard_normal((atoms.Nspin, len(atoms.G2c), atoms.Nstate))
    else:
        W = rng.standard_normal((atoms.Nspin, len(atoms.G2c), atoms.Nstate))
    return orth(atoms, W)


def guess_gaussian(scf, complex=True):
    '''Generate initial-guess coefficients using normalized Gaussians as starting values.

    Args:
        scf: SCF object.

    Keyword Args:
        complex (bool): Use complex numbers for the random guess.

    Returns:
        ndarray: Initial-guess orthogonal wave functions in reciprocal space.
    '''
    atoms = scf.atoms
    # Start with randomized wave functions
    W = guess_random(scf, complex=complex)

    sigma = 0.5
    normal = (2 * np.pi * sigma**2)**(3 / 2)
    # Calculate a density from normalized Gauss functions
    n = np.zeros(len(atoms.r)) + 1e-15  # Add a small epsilon to prevent divisions by zero in exc
    for ia in range(atoms.Natoms):
        r = norm(atoms.r - atoms.X[ia], axis=1)
        n += atoms.Z[ia] * np.exp(-r**2 / (2 * sigma**2)) / normal
    # Calculate the eigenfunctions
    return get_psi(scf, W, n)


def guess_pseudo(scf, seed=1234):
    '''Generate initial-guess coefficients using pseudo-random starting values.

    Args:
        scf: SCF object.

    Keyword Args:
        seed (int): Seed to initialize the random number generator.

    Returns:
        ndarray: Initial-guess orthogonal wave functions in reciprocal space.
    '''
    atoms = scf.atoms
    W = pseudo_uniform((atoms.Nspin, len(atoms.G2c), atoms.Nstate), seed=seed)
    return orth(atoms, W)
