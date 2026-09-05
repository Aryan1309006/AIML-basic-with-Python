import numpy as np
# =========================
# 1️⃣5️⃣ LINEAR ALGEBRA
# =========================

print("\n========== LINEAR ALGEBRA ==========")

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("\nDot Product:\n", np.dot(A, B))
print("Matrix Multiplication:\n", np.matmul(A, B))
print("\nDeterminant of A:", np.linalg.det(A))
print("\nInverse of A:\n", np.linalg.inv(A))

eigen_values, eigen_vectors = np.linalg.eig(A)
print("\nEigenvalues:", eigen_values)
print("Eigenvectors:\n", eigen_vectors)


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