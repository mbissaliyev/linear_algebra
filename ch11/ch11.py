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
