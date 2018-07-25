# chapter 6 - numpy array broadcasting

import numpy as np

a = [1, 2, 3]
b = [1, 2, 3]
c = a + b
print(c)

# a = [a1, a2, a3]
# b = [b1, b2, b3]
# c = a + b


# broadcast scalar array
a = np.array([1, 2, 3])
print(a)

b = 4
# print(b)

c = a + b
print(c)

# broadcast to 2D array

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("Array A:", A)

# define scalar value

b = 2
print("Scalar b:", b)
c = A + b
print("Array C:", c)

# broadcast 1D array to 2D array

# 2D array
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("A:", A)

b = np.array([1, 2, 3])
print("b:", b)

C = A + b
print("C:", C)


# broadcasting error
A = np.array([[1,2,3],
              [4,5,6]])
print("A:", A.shape)

# 1D array
b = np.array([1,2])
print(b.shape)
c = A + b
print(c)


