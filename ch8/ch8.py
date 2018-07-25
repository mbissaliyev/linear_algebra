# Vector Norms - vector lengs and magnitutdes

# 1 Vector Norms
import numpy as np

# define vector
a = np.array([1, 2, 3])
print(a)

# calculate L-1 NORM = L1 = A[0] + A[1] + A[2]

l1 = np.linalg.norm(a, 1)
print(l1)

# L-2 Norm = L2 = SQRT(A[0]^2 + A[1]^2 + A[2]^2)
l2 = np.linalg.norm(a)
print(l2)

# Vector MAX-NORM = max(A[0],A[1] A[2])
maxnorm = np.linalg.norm(a, np.inf)
print(maxnorm)
