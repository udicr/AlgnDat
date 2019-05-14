import numpy as np
import scipy
import scipy.linalg
import time

eps = 1.0 / np.power(10, 16)


def a_skalar(A, u, w):
    return u.transpose() * A * w


def a_norm(x, A):
    return np.sqrt(a_skalar(A, x, x))


def _1_norm(x):
    return sum(np.abs(x[:, 0]))


def eukl_norm(x):
    return np.sqrt(x.transpose().__matmul__(x)[0][0])


def max_norm(x):
    return np.amax(np.abs(x))  # max value ls(i:)


def LUdecomp(A):
    '''
    basic funcion of LUDecomp in single notation
    :param A: np.matrix() nxn
    :return:  LR np.matrix() can be splitted to L and U with funcs below
    '''
    n = A[0].size
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if A[k, k] != 0.0:
                lam = A[i, k] / A[k, k]
            A[i, k + 1:n] = A[i, k + 1:n] - lam * A[k, k + 1:n]
            A[i, k] = lam
    return A


def cholesky_solve(A, b):
    n = A[0].size
    for i in range(n):
        A[i + 1:, i] = A[i + 1:, i] * 1.0 / A[i, i]
        A[i + 1:, i + 1:] = A[i + 1:, i + 1:] - A[i + 1:, i] * A[i, i + 1:]

    x = b
    for i in range(1, n):
        x[i] = x[i] - A[i, :i] * x[:i]

    for i in range(n - 1, -1, -1):
        x[i] = (x[i] - A[i, i + 1:n + 1] * x[i + 1:n + 1]) / A[i, i]
    return x


def LUP_solve(A, b):
    '''
    :param A: np.matrix() nxn
    :param b: np.array() shape(1,n)
    :return: x: np.array() shape(1,n)
    '''
    n = A[0].size
    p = np.array(range(0, n))

    for i in range(0, n - 1):
        r = np.amax(np.abs(A[i:, i]))  # max value ls(i:)
        m = np.where(np.abs(A[i:, i]) == r)[0][0] + i  # max index ls(i:)
        if np.abs(A[m, n - 1]) < eps:
            raise ZeroDivisionError("Matrix fast singulär")
        if m != i:
            A[[i, m]] = A[[m, i]]

            p[[i, m]] = p[[m, i]]

        A[i + 1:, i] = A[i + 1:, i] * 1.0 / A[i, i]
        A[i + 1:, i + 1:] = A[i + 1:, i + 1:] - A[i + 1:, i] * A[i, i + 1:]

    # x = b

    x = b[p]

    for i in range(1, n):
        x[i] = x[i] - A[i, :i] * x[:i]

    for i in range(n - 1, -1, -1):
        x[i] = (x[i] - A[i, i + 1:n + 1] * x[i + 1:n + 1]) / A[i, i]
    return x


def get_ru(A):
    return np.triu(A)


def get_ll(A):
    n = A[0].size
    return np.tril(A, -1) + np.diag(np.ones(n))



