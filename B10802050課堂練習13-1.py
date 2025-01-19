import numpy as np
A = input('輸入 2*2 矩陣 A 的四個值，ˊ之間以空白隔開：')
A = A.split()
A = np.array([[int(A[0]), int(A[1])],
              [int(A[2]), int(A[3])]])

try:
    B = np.linalg.inv(A)
    print(B)
except Exception:
    print('A的反矩陣不存在')
