# Copyright 2023 Krzysztof Wiśniewski <argmaster.world@gmail.com>
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the “Software”), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# ------------------------------------------------------------------------------------ #
#                                                                                      #
#   THIS FILE WAS AUTOMATICALLY GENERATED FROM TEMPLATE. DO NOT MODIFY.                #
#                                                                                      #
#   To modify this file, modify `scripts/templates/numpy.pyjinja2` and                 #
#   use `poe gen-numpy-impl` to generate python files.                                 #
#                                                                                      #
# ------------------------------------------------------------------------------------ #
#
"""Module contains implementation of backend operations in numpy.

Spec
----

- Floating precision:   np.float32
- Complex precision:    np.complex64

"""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
from numba import jit, types  # type: ignore[attr-defined]

if TYPE_CHECKING:
    import numpy.typing as npt


#    █████  ██████  ███    ███ ███    ███  ██████  ███    ██
#   ██     ██    ██ ████  ████ ████  ████ ██    ██ ████   ██
#   ██     ██    ██ ██ ████ ██ ██ ████ ██ ██    ██ ██ ██  ██
#   ██     ██    ██ ██  ██  ██ ██  ██  ██ ██    ██ ██  ██ ██
#    █████  ██████  ██      ██ ██      ██  ██████  ██   ████


_REAL = np.cos(0.01 * np.pi)
_IMAG = 1j * np.sin(0.01 * np.pi)
_VALUE = (_REAL + _IMAG - 1).astype(np.complex64)


@jit(nopython=True, nogil=True, cache=True)
def product(
    matrix1: npt.NDArray[np.complex64], matrix2: npt.NDArray[np.complex64]
) -> np.float32:
    """Calculate scalar product of two matrices."""
    retval = np.trace(np.dot(matrix1, matrix2)).real

    return retval  # type: ignore[no-any-return]


@jit(nopython=True, nogil=True, cache=True)
def get_random_haar_1d(depth: int) -> npt.NDArray[np.complex64]:
    """Generate a random vector with Haar measure."""
    real = np.random.uniform(0, 1, depth)  # noqa: NPY002
    imag = np.random.uniform(0, 1, depth)  # noqa: NPY002

    retval = np.exp(2 * np.pi * 1j * real) * np.sqrt(-np.log(imag))

    retval = (retval).astype(np.complex64)

    return retval  # type: ignore[no-any-return]


@jit(nopython=True, nogil=True, cache=True)
def get_random_haar_2d(depth: int, quantity: int) -> npt.NDArray[np.complex64]:
    """Generate multiple random vectors with Haar measure in form of matrix."""
    real = np.random.uniform(0, 1, (quantity, depth))  # noqa: NPY002
    imag = np.random.uniform(0, 1, (quantity, depth))  # noqa: NPY002

    retval = np.exp(2 * np.pi * 1j * real) * np.sqrt(-np.log(imag))

    retval = (retval).astype(np.complex64)

    return retval  # type: ignore[no-any-return]


@jit(nopython=True, nogil=True, cache=True)
def normalize(mtx: npt.NDArray[np.complex64]) -> npt.NDArray[np.complex64]:
    """Normalize a vector."""
    mtx2 = np.dot(mtx, np.conj(mtx))

    val = np.sqrt(np.real(mtx2))

    retval = mtx / val

    return retval  # type: ignore[no-any-return]


@jit(nopython=True, nogil=True, cache=True)
def project(mtx1: npt.NDArray[np.complex64]) -> npt.NDArray[np.complex64]:
    """Build a projection from a vector."""
    retval = np.outer(mtx1, np.conj(mtx1))

    return retval  # type: ignore[no-any-return]


@jit(nopython=False, forceobj=True, cache=True, looplift=False)
def kronecker(
    mtx: npt.NDArray[np.complex64], mtx1: npt.NDArray[np.complex64]
) -> npt.NDArray[np.complex64]:
    """Kronecker Product."""
    ddd1 = len(mtx)
    ddd2 = len(mtx1)

    output_shape = (ddd1 * ddd2, ddd1 * ddd2)

    dot_0_1 = np.tensordot(mtx, mtx1, 0)

    out_mtx = np.swapaxes(dot_0_1, 1, 2)

    retval = out_mtx.reshape(output_shape).astype(np.complex64, copy=False)

    return retval  # type: ignore[no-any-return]


@jit(nopython=True, nogil=True, cache=True)
def rotate(
    rho2: npt.NDArray[np.complex64], unitary: npt.NDArray[np.complex64]
) -> npt.NDArray[np.complex64]:
    """Sandwich an operator with a unitary."""
    rho2a = np.dot(rho2, np.conj(unitary).T)  # matmul replaced with dot

    rho2a = np.dot(unitary, rho2a)  # matmul replaced with dot

    return rho2a  # type: ignore[no-any-return]


@jit(nopython=True, nogil=True, cache=True)
def apply_symmetries(
    rho: npt.NDArray[np.complex64],
    symmetries: types.ListType[types.ListType[npt.NDArray[np.complex64]]],
) -> npt.NDArray[np.complex64]:
    """Apply symmetries to density matrix.

    Parameters
    ----------
    rho : npt.NDArray[np.complex64]
        Density matrix to which we want to apply symmetries.
    symmetries : list[list[npt.NDArray[np.complex64]]]
        List of matrices representing the symmetries.

    Returns
    -------
    npt.NDArray[np.complex64]
        The result of applying the symmetries to the given density matrix.

    Notes
    -----
    The first input `rho` is modified by this function. If you don't want to modify the
    original array, make a copy before passing it to this function.

    This function calculates the trace of output density matrix and normalizes it before
    returning.

    """
    output = rho
    for row in symmetries:
        for sym in row:
            output += rotate(output, sym)

    output /= np.trace(output)
    return output


#   ██████     ███████    ███████            ███    ███     ██████     ██████     ███████   # noqa: E501
#   ██   ██    ██         ██                 ████  ████    ██    ██    ██   ██    ██        # noqa: E501
#   ██   ██    █████      ███████            ██ ████ ██    ██    ██    ██   ██    █████     # noqa: E501
#   ██   ██    ██              ██            ██  ██  ██    ██    ██    ██   ██    ██        # noqa: E501
#   ██████     ██         ███████            ██      ██     ██████     ██████     ███████   # noqa: E501


@jit(nopython=False, forceobj=True, cache=True, looplift=False)
def optimize_d_fs(
    new_state: npt.NDArray[np.complex64],
    visibility_state: npt.NDArray[np.complex64],
    depth: int,
    quantity: int,
) -> npt.NDArray[np.complex64]:
    """Optimize implementation for FSnQd mode."""
    loss = product(new_state, visibility_state)

    # To make sure return_state is not unbound
    unitary = random_unitary_d_fs(depth, quantity, 0)

    return_state = rotate(new_state, unitary)

    for idx in range(20 * depth * depth * quantity):
        idx_mod = idx % int(quantity)
        unitary = random_unitary_d_fs(depth, quantity, idx_mod)

        return_state = rotate(new_state, unitary)

        new_loss = product(return_state, visibility_state)

        if loss > new_loss:
            unitary = unitary.conj().T
            return_state = rotate(new_state, unitary)

        while new_loss > loss:
            loss = new_loss
            return_state = rotate(return_state, unitary)

            new_loss = product(return_state, visibility_state)

    return return_state.astype(np.complex64, copy=False)  # type: ignore[no-any-return]


@jit(nopython=False, forceobj=True, cache=True, looplift=False)
def random_unitary_d_fs(
    depth: int, quantity: int, idx: int
) -> npt.NDArray[np.complex64]:
    """N quDits."""
    value = _random_unitary_d_fs(depth)

    mtx = expand_d_fs(value, depth, quantity, idx)

    return mtx  # type: ignore[no-any-return]


@jit(nopython=True, nogil=True, cache=True)
def _random_unitary_d_fs(depth: int) -> npt.NDArray[np.complex64]:
    random_mtx = random_d_fs(depth, 1)

    identity_mtx = np.identity(depth).astype(np.complex64)

    rand_mul = np.multiply(_VALUE, random_mtx)

    value = np.add(rand_mul, identity_mtx)

    return value  # type: ignore[no-any-return]


@jit(nopython=True, nogil=True, cache=True)
def random_d_fs(depth: int, quantity: int) -> npt.NDArray[np.complex64]:
    """Random n quDit state."""
    rand_vectors = get_random_haar_2d(depth, quantity)
    vector = normalize(rand_vectors[0])

    for i in range(1, quantity):
        idx_vector = normalize(rand_vectors[i])

        vector = np.outer(vector, idx_vector).flatten()

    vector = project(vector)

    return vector  # type: ignore[no-any-return]


@jit(nopython=False, forceobj=True, cache=True, looplift=False)
def expand_d_fs(
    value: npt.NDArray[np.complex64],
    depth: int,
    quantity: int,
    idx: int,
) -> npt.NDArray[np.complex64]:
    """Expand an operator to n quDits."""
    depth_1 = int(depth**idx)
    identity_1 = np.identity(depth_1, dtype=np.complex64)

    depth_2 = int(depth ** (quantity - idx - 1))
    identity_2 = np.identity(depth_2, dtype=np.complex64)

    kronecker_1 = kronecker(identity_1, value)

    kronecker_2 = kronecker(kronecker_1, identity_2)

    return kronecker_2  # type: ignore[no-any-return]


#   ██████     ███████            ███    ███     ██████     ██████     ███████
#   ██   ██    ██                 ████  ████    ██    ██    ██   ██    ██
#   ██████     ███████            ██ ████ ██    ██    ██    ██   ██    █████
#   ██   ██         ██            ██  ██  ██    ██    ██    ██   ██    ██
#   ██████     ███████            ██      ██     ██████     ██████     ███████


@jit(nopython=True, nogil=True, cache=True)
def random_bs(depth: int, quantity: int) -> npt.NDArray[np.complex64]:
    """Draw random biseparable state."""
    random_vector_1 = normalize(get_random_haar_1d(depth))
    random_vector_2 = normalize(get_random_haar_1d(quantity))

    vector = np.outer(random_vector_1, random_vector_2).flatten()

    vector = project(vector)

    return vector  # type: ignore[no-any-return]


@jit(nopython=False, forceobj=True, cache=True, looplift=False)
def random_unitary_bs(depth: int, quantity: int) -> npt.NDArray[np.complex64]:
    """Draw random unitary for biseparable state."""
    random_vector = normalize(get_random_haar_1d(depth))

    random_matrix = project(random_vector)

    identity_depth = np.identity(depth).astype(np.complex64)

    identity_quantity = np.identity(quantity).astype(np.complex64)

    unitary_biseparable = _VALUE * random_matrix + identity_depth

    retval = kronecker(unitary_biseparable, identity_quantity)

    return retval  # type: ignore[no-any-return]


@jit(nopython=False, forceobj=True, cache=True, looplift=False)
def random_unitary_bs_reverse(quantity: int, depth: int) -> npt.NDArray[np.complex64]:
    """Draw random unitary for biseparable state."""
    random_vector = normalize(get_random_haar_1d(depth))

    random_matrix = project(random_vector)

    identity_depth = np.identity(depth).astype(np.complex64)

    identity_quantity = np.identity(quantity).astype(np.complex64)

    unitary_biseparable = _VALUE * random_matrix + identity_depth

    retval = kronecker(identity_quantity, unitary_biseparable)

    return retval  # type: ignore[no-any-return]


@jit(nopython=False, forceobj=True, cache=True, looplift=False)
def optimize_bs(
    new_state: npt.NDArray[np.complex64],
    visibility_state: npt.NDArray[np.complex64],
    depth: int,
    quantity: int,
) -> npt.NDArray[np.complex64]:
    """Run the minimization algorithm to optimize the biseparable state.

    Parameters
    ----------
    new_state : npt.NDArray[np.complex64]
        Randomly drawn state to be optimized.
    visibility_state : npt.NDArray[np.complex64]
        Visibility matrix.
    depth : int
        Depth of analyzed system.
    quantity : int
        Quantity of quDits in system.
    updates_count : int
        Number of optimizer iterations to execute.

    Returns
    -------
    npt.NDArray[np.complex64]
        Optimized state.

    """
    loss = product(new_state, visibility_state)

    return_state = new_state.copy()

    for index in range(5 * depth * quantity):
        if index % 2:
            unitary = random_unitary_bs(depth, quantity)
        else:
            unitary = random_unitary_bs_reverse(depth, quantity)

        return_state = rotate(new_state, unitary)

        if loss > product(return_state, visibility_state):
            unitary = unitary.conj().T
            return_state = rotate(new_state, unitary)

        new_loss = product(return_state, visibility_state)

        while new_loss > loss:
            loss = new_loss
            return_state = rotate(return_state, unitary)
            new_loss = product(return_state, visibility_state)

    return return_state


#    ███████   █████▄   ██████     █████    ███████   ██████▄    ██████    ██████
#   ██             ██   ██   ██   ██   ██   ██             ██   ██    ██   ██   ██
#   ██   ███   █████    ██████    ███████   █████      █████    ██    ██   ██   ██
#   ██    ██       ██   ██        ██   ██   ██             ██   ██ ▄▄ ██   ██   ██
#    ███████   █████▀   ██        ██   ██   ███████   ██████▀    ██████    ██████
#                                                                   ▀▀


@jit(nopython=True, nogil=True, cache=True)
def random_3p(
    depth: int,
    swaps: types.ListType[npt.NDArray[np.complex64]],
    index: int,
) -> npt.NDArray[np.complex64]:
    """Draw random biseparable state."""
    if index == 0:
        return random_bs(depth, depth * depth)  # type: ignore[no-any-return]
    if index == 1:
        return rotate(  # type: ignore[no-any-return]
            random_bs(depth, depth * depth),
            swaps[0],
        )

    return random_bs(depth * depth, depth)  # type: ignore[no-any-return]


OPTIMIZE_3P_OPT_0 = 0
OPTIMIZE_3P_OPT_1 = 1
OPTIMIZE_3P_OPT_2 = 2


OPTIMIZE_3P_JUMP_TABLE = [random_unitary_bs, random_unitary_bs_reverse]


@jit(nopython=False, forceobj=True, cache=True, looplift=False)
def optimize_3p(
    new_state: npt.NDArray[np.complex64],
    visibility_state: npt.NDArray[np.complex64],
    depth: int,
    swaps: types.ListType[npt.NDArray[np.complex64]],
    index: int,
) -> npt.NDArray[np.complex64]:
    return_state = new_state.copy()
    loss = product(new_state, visibility_state)

    for i in range(5 * depth**6):
        if index == OPTIMIZE_3P_OPT_0:
            unitary = OPTIMIZE_3P_JUMP_TABLE[i % 2](depth, depth * depth)

        elif index == OPTIMIZE_3P_OPT_1:
            unitary = OPTIMIZE_3P_JUMP_TABLE[i % 2](depth, depth * depth)
            unitary = rotate(unitary, swaps[0])

        elif index == OPTIMIZE_3P_OPT_2:
            unitary = OPTIMIZE_3P_JUMP_TABLE[i % 2](depth * depth, depth)

        return_state = rotate(new_state, unitary)

        new_loss = product(return_state, visibility_state)

        if loss > new_loss:
            unitary = unitary.conj().T
            return_state = rotate(new_state, unitary)
            new_loss = product(return_state, visibility_state)

        while new_loss > loss:
            loss = new_loss
            return_state = rotate(return_state, unitary)

            new_loss = product(return_state, visibility_state)

    return return_state  # type: ignore[no-any-return]
