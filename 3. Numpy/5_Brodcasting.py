
# =========================
#   5.BROADCASTING
# =========================
import numpy as np

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)
print(array1*array2)

"""
===========================
        Output
===========================
(1, 4)
(4, 1)
[[ 1  2  3  4]
 [ 2  4  6  8]
 [ 3  6  9 12]
 [ 4  8 12 16]]

"""