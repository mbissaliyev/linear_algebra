# Type of Matrices

# Square Matrix n===m

import numpy as np

M = np.array([[1, 2, 3],
              [1, 2, 3],
              [1, 2, 3]])
print(M)

print("Triangular lower:", np.tril(M))

print("Triangular lower:", np.triu(M))

# Diagonal Matrix

# step 1 - extract diagonal vector
d = np.diag(M)

# step 2 - create diagonal matrix from vector
D = np.diag(d)
print("Diagonal", D)
