# Matrices and Matrix Arithmetic

import numpy as np

# create matrix

A = np.array([[1, 2, 3],
              [3, 4, 5]])
print(A)

B = np.array([[1, 2, 3],
              [3, 4, 5]])
print(B)

# multiplication
C = A * B
print(C)

# substraction
C = A - B
print(C)

# Matrix x Matrix multiplication

A = np.array([[1, 2],
              [3, 4],
              [5, 6]])
B = np.array([[1, 2],
              [3, 4]])
C = A.dot(B)
print(C)

# Matrix Vector Multiplication
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])
B = np.array([0.5, 0.5])
C = A.dot(B)
print("C:", C)
