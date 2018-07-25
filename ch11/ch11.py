# Matrix Operations

# Transpose

import numpy as np

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

print(A)
print(A.T)

# Inverse
A = np.array([[1, 2],
              [3, 4]])

B = np.linalg.inv(A)
print(B)

# multiply A x B
C = A.dot(B)
print(C)

# Trace - calculate diagonal values from top left to right bottom
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(A)
B = np.trace(A)
print(B)

# Determinant - scalar representation of the volument of the matrix
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(A)
B = np.linalg.det(A)
print(B)


# Rank - linearly independent rows

A = np.array([1,2,3])
vr1 = np.linalg.matrix_rank(A)
print(vr1)

B = np.array([0,0,0,0])
vr2 = np.linalg.matrix_rank(B)
print(vr2)

A = np.array([[1,2],
              [3,4]])
vr1 = np.linalg.matrix_rank(A)
print(vr1)



