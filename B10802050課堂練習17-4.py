import numpy as np

A = np.array([[1, 1, 1, 1], [2, 2, 1, 1], [3, 3, 2, 2]])
# print(A, '\n')

A11 = A[:2, :2]
A12 = A[:2, 2:]
A21 = A[2:, :2]
A22 = A[2:, 2:]

B = np.array([[1, 1, 1, 1], [1, 2, 1, 1], [3, 1, 1, 1], [3, 2, 1, 2]])
# print(B, '\n')

B11 = B[:2, :2]
B12 = B[:2, 2:]
B21 = B[2:, :2]
B22 = B[2:, 2:]

C = np.dot(A, B)
print(C, '\n')

C11 = np.dot(A11, B11) + np.dot(A12, B21)
C12 = np.dot(A11, B12) + np.dot(A12, B22)
C21 = np.dot(A21, B11) + np.dot(A22, B21)
C22 = np.dot(A21, B12) + np.dot(A22, B22)

print(C11, '\n')
print(C12, '\n')
print(C21, '\n')
print(C22, '\n')
