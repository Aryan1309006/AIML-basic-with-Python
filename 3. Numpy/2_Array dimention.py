# =========================
#   2.ARRAY DIMENSIONS
# =========================

import numpy as np 
# 1D array
array = np.array([1])
print("1D array:",array.ndim)

# 2D array
array = np.array([
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
])
print("2D array:", array.ndim)

# 3D array
array = np.array([
    [['a','b','c'],['d','e','f'],['g','h','i']],
    [['a','b','c'],['d','e','f'],['g','h','i']],
    [['a','b','c'],['d','e','f'],['g','h','i']]
])
print("2D array:", array.ndim)

# Element access (modern NumPy indexing)
print("Element [0,0,0]:",array[0,0,0])

# String concatenation from array elements
word = array[0,0,0] + array[0,1,2] + array[1,2,0]
print("word:",word)

# Shape of array (depth, rows, columns)
print("shape:",array.shape)

"""
===========================
        Output
===========================
1D array: 1
2D array: 2
2D array: 3
Element [0,0,0]: a
word: afg
shape: (3, 3, 3)

"""