import numpy as np
from scipy.linalg import svd

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(A)

#factorize
U, s, VT = svd(A)
print(U)
print(s)
print(VT)


# create m x n Sigma matrix
Sigma = np.zeros((A.shape[0], A.shape[1]))

Sigma[:A.shape[1], :A.shape[1]] =np.diag(s)

B = U.dot(Sigma.dot(VT))
print(B)