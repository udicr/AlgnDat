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
            # A[[i, m], :] = A[[m, i], :]                                       #todo: works without pivot solving but doesnt with

            p[[i, m]] = p[[m, i]]
        A[i + 1:, i] = A[i + 1:, i] * 1.0 / A[i, i]
        A[i + 1:, i + 1:] = A[i + 1:, i + 1:] - A[i + 1:, i] * A[i, i + 1:]
    print(A)
    x = b
    # x = b[p]
    print(x)
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


A = np.matrix([[2, 0, 0, 1],
               [4, 1, 0, 2],
               [6, 2, 3, 3],
               [8, 3, 6, 8]])
b = np.array([[3],
              [7],
              [14],
              [25]])
'''print(A)
t0 = time.time()
P, L, U = scipy.linalg.lu(A,True)
print(L)
t1 = time.time() - t0
t0 += t1
print(LU_einzeln(A))
t2 = time.time() - t0
print("T1 : " + str(t1) + "  T2 : " + str(t2))
'''
x = LUP_solve(A, b)

A = np.matrix([[2, 0, 0, 1],
               [4, 1, 0, 2],
               [6, 2, 3, 3],
               [8, 3, 6, 8]])
print(LUdecomp(A))
print(_1_norm(x))
