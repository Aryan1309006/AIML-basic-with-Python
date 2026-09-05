# =========================
# 1️⃣2️⃣ RANDOM NUMBERS
# =========================
import numpy as np

rng = np.random.default_rng(seed=1)
print(rng.integers(low=1,high=7,size=3))

print(np.random.uniform(low=-1,high=1,size=(3,2)))

array = np.array([1,2,3,4])
rng.shuffle(array)
print(array)

array = np.array([1,2,3,4])
rand = rng.choice(array)
print(rand)


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