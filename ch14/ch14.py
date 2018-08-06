# Chapter 14 matrix decomposition

import numpy as np
from scipy.linalg import lu
from scipy.linalg import qr

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

])

print(A)

P, L, U = lu(A)
print(P)
print(L)
print(U)

# reconstruct
B = P.dot(L).dot(U)
print(B)

# QR decomposition

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(A)

Q, R = qr(A)
print(Q)
print(R)

# reconstruct
B = Q.dot(R)
print(B)

from numpy.linalg import cholesky

A = np.array([
    [2, 1, 1],
    [1, 2, 1],
    [1, 1, 2],

])

print(A)

L = cholesky(A)
print(L)

#reconstruct
B = L.dot(L.T)
print(B)