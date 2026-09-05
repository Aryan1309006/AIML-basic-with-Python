import numpy as np
# =========================
# 1️⃣4️⃣ STACKING & SPLITTING
# =========================

print("\n========== STACKING & SPLITTING ==========")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)

print("\nVertical Stack:\n", np.vstack((a, b)))
print("Horizontal Stack:", np.hstack((a, b)))
print("Concatenated:", np.concatenate((a, b)))

array_to_split = np.array([10, 20, 30, 40, 50, 60])
print("\nSplit array into 3 parts:", np.split(array_to_split, 3))


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