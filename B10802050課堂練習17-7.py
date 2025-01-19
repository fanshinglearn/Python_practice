import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 2, 3], [3, 2, 1]])
c = np.array([[1], [-1]])
d = np.array([[1], [2]])

print(np.dot(A, B))
print(np.inner(c, d))
print(np.linalg.det(A))
print(np.linalg.inv(A))
print(np.diag(A))
print(np.linalg.matrix_power(A, 10))
print(np.linalg.solve(A, c))
