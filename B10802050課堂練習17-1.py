import numpy as np

A = np.zeros([9, 9], dtype=np.int32)

for i in range(9):
    for j in range(9):
        x = j + i + 1
        A[i][j] = 18 - x if x > 9 else x
print(A)

A = A.astype(np.float64)
print(A)
