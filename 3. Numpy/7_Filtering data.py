import numpy as np
# =========================
#   7.FILTERING DATA
# =========================

ages = np.array([
    [21,17,20,16,65],
    [39,22,15,99,18]
])

teenagers = ages[ages<18]
print("Teenagers:",teenagers)

print("Even:",ages[ages%2==0])

# Conditional replacement
adults = np.where(ages>=18,ages,0)
print("Adult:",adults)


"""
===========================
        Output
===========================
Teenagers: [17 16 15]
Even: [20 16 22 18]
Adult: [[21  0 20  0 65]
 [39 22  0 99 18]]

"""