import numpy as np
# =========================
# 🔟 AGGREGATE FUNCTIONS
# =========================

array = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

print("Sum:",np.sum(array))
print("Mean",np.mean(array))
print("Standard deviation:",np.std(array))      # Standard deviation
print("Variance:",np.var(array))      # Variance
print("Minimum value:",np.min(array))
print("Maximum value",np.max(array))
print("Index of min value",np.argmin(array))   # Index of min value
print("Index of max value",np.argmax(array))   # Index of max value
print("sum:",np.sum(array,axis=0))


"""
===========================
        Output
===========================
Sum: 36
Mean 4.5
Standard deviation: 2.29128784747792
Variance: 5.25
Minimum value: 1
Maximum value 8
Index of min value 0
Index of max value 7
sum: [ 6  8 10 12]

"""