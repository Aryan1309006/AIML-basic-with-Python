import numpy as np
# =========================
# 1️⃣6️⃣ HANDLING MISSING DATA
# =========================

print("\n========== HANDLING MISSING DATA ==========")

data = np.array([10, 20, np.nan, 40, np.nan, 60])
print("Original data:", data)

print("Is NaN?:", np.isnan(data))

mean_without_nan = np.nanmean(data)
print("Mean without NaN:", mean_without_nan)

print("NaN replaced with 0:", np.nan_to_num(data, nan=0))
print("NaN replaced with mean:", np.nan_to_num(data, nan=mean_without_nan))


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