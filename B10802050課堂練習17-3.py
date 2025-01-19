import numpy as np

A = np.array([[1, 1, 1, 1], [2, 2, 1, 1], [3, 3, 2, 2]])
print(A, '\n')

A11 = A[:2, :2]
A12 = A[:2, 2:]
A21 = A[2:, :2]
A22 = A[2:, 2:]

print(A11, '\n')
print(A12, '\n')
print(A21, '\n')
print(A22, '\n')

B = np.array([[1, 1, 1, 1], [1, 2, 1, 1], [3, 1, 1, 1], [3, 2, 1, 2]])
print(B, '\n')

B11 = B[:2, :2]
B12 = B[:2, 2:]
B21 = B[2:, :2]
B22 = B[2:, 2:]

print(B11, '\n')
print(B12, '\n')
print(B21, '\n')
print(B22, '\n')
