
import numpy as np
# =========================
#   4️.SCALAR ARITHMETIC
# =========================

array = np.array([1,2,3,4])
print("arr+1",array+1)
print("arr-2",array-2)
print("arr*2",array*2)
print("arr/2",array/2)
print("arr**2",array**2)
print("\n")

# =========================
#    VECTORIZED MATH
# =========================

array = np.array([1.2,2.5,3.1,4.4])
print("Array:",array)
print("Squre root:",np.sqrt(array))
print("Rounded value:",np.round(array))
print("floor:",np.floor(array))
print("ceil:",np.ceil(array))
print("valu of pi:",np.pi)
print("\n")

# =========================
#   ELEMENT-WISE OPERATIONS
# =========================

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print("Addition", (array1+array2))
print("Subtraction:",array1-array2)
print("Multiplication:",array1*array2)
print("Division:",array1/array2)
print("\n")

# =========================
#   COMPARISON & MASKING
# =========================

score = np.array([91,55,100,73,82,64])
print("Score:",score)

print("score=100",score==100)
print("score>=60",score>=60)

# Replace values < 60 with 0
score[score<60] = 0
print("score<60 is 0:",score)
print("\n")

# =========================
# PRACTICAL EXERCISE
# =========================

# Area of circle: πr²
radii = np.array([1,2,3])
print(radii)
print((np.pi) * radii ** 2)



"""
===========================
        Output
===========================
arr+1 [2 3 4 5]
arr-2 [-1  0  1  2]
arr*2 [2 4 6 8]
arr/2 [0.5 1.  1.5 2. ]
arr**2 [ 1  4  9 16]


Array: [1.2 2.5 3.1 4.4]
Squre root: [1.09544512 1.58113883 1.76068169 2.0976177 ]
Rounded value: [1. 2. 3. 4.]
floor: [1. 2. 3. 4.]
ceil: [2. 3. 4. 5.]
valu of pi: 3.141592653589793


Addition [5 7 9]
Subtraction: [-3 -3 -3]
Multiplication: [ 4 10 18]
Division: [0.25 0.4  0.5 ]


Score: [ 91  55 100  73  82  64]
score=100 [False False  True False False False]
score>=60 [ True False  True  True  True  True]
score<60 is 0: [ 91   0 100  73  82  64]


[1 2 3]
[ 3.14159265 12.56637061 28.27433388]

"""