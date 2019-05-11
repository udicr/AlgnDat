import numpy as np
import scipy
import scipy.linalg
import time


eps = 1.0 / np.power(10, 16)


def a_skalar(A, u, w):
    return u.transpose() * A * w


def a_norm(x, A):
    return np.sqrt(a_skalar(A, x, x))


def LU_einzeln(A):
    '''
    inplace
    :param A: np.matrix()  nxn
    :return: LR np.matrix() saved in one matrix  nxn
    '''
    n = A[0].size

    for k in range(n):
        if np.abs(A[k, k]) < eps:
            raise ZeroDivisionError("LR - Zerlegung exitiert nicht")

        for i in range(k +1, n):
            A[i, k] = A[i, k] / A[k, k]
            for j in range(k +1, n):
                A[i, j] = A[i, j] - A[i, k] * A[k, j]
    return A


def get_ru(A):
    return np.triu(A)


def get_ll(A):
    n = A[0].size
    return np.tril(A, -1) + np.diag(np.ones(n))


A = np.matrix([[1, 4, 3, 2],
               [3, 1, 2, 1],
               [1, 2, 1, 1],
               [1, 1, 5, 1]])
print(A)
t0 = time.time()
P, L, U = scipy.linalg.lu(A,True)
print(L)
t1 = time.time() - t0
t0 += t1
print(LU_einzeln(A))
t2 = time.time() - t0
print("T1 : " + str(t1) + "  T2 : " + str(t2))

