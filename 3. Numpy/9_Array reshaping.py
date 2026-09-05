import numpy as np
# =========================
# 1️⃣3️⃣ ARRAY RESHAPING
# =========================

print("========== ARRAY RESHAPING ==========")

array = np.array([1, 2, 3, 4])
print("Original array:", array)
print("Shape:", array.shape)

reshaped = array.reshape(2, 2)
print("\nReshaped (2x2):\n", reshaped)
print("Shape:", reshaped.shape)

flattened = reshaped.flatten()
print("\nFlattened array:", flattened)

raveled = reshaped.ravel()
print("Raveled array:", raveled)

transposed = reshaped.T
print("\nTransposed array:\n", transposed)


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