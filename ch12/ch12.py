# chapter 12 - Sparse matrices

import numpy as np
from scipy.sparse import csr_matrix
from numpy import count_nonzero
# create array
A = np.array([
    [1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0]

])

print(A)

# convert to compressed sparse row
S = csr_matrix(A)
print(S)

B = S.todense()
print(B)

sparsirty = float(1.0) - np.count_nonzero(A) / np.size()
print(sparsirty)