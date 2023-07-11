import numpy as np


# SciPy has a module, scipy.sparse that provides functions to deal with sparse data.
# There are primarily two types of sparse matrices that we use:
# CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
# CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products
# We will use the CSR matrix in this tutorial.
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))
# From the result we can see that there are 3 items with value.
# The 1. item is in row 0 position 5 and has the value 1.


# Sparse Matrix Methods
# Viewing stored data (not the zero items) with the data property:
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data)
# Counting nonzeros with the count_nonzero() method:
print(csr_matrix(arr).count_nonzero())
