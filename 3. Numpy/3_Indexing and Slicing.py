# =========================
#   3️.INDEXING & SLICING
# =========================
import numpy as np

array = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

print("array[1]",array[1])          # Second row
print("last row usin -1:",array[-1])

# Slicing rows (start:end)
print("Array after slicing:",array[1:4])


"""
===========================
        Output
===========================
array[1] [5 6 7 8]
last row usin -1: [13 14 15 16]
Array after slicing: [[ 5  6  7  8]
                    [ 9 10 11 12]
                    [13 14 15 16]]

"""