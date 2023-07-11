import numpy as np 
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr= np.array([
    [0,1,2],
    [3,0,0],
    [6,7,0]
])
new_arr = csr_matrix(arr)
print(connected_components(new_arr))