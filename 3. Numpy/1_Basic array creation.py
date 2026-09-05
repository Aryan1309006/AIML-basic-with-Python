import numpy as np 

# =========================
#   1.BASIC ARRAY CREATION
# =========================

array = np.array([1,2,3,4])
print("array:",array)
print("type:",type(array))

# Vectorized multiplication
array = array * 2
print("arrya*2:",array)

""""
===========================
        Output
===========================
array: [1 2 3 4]
type: <class 'numpy.ndarray'>
arrya*2: [2 4 6 8]

"""