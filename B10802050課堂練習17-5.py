import numpy as np

A = np.array([[1, 1], [2, 2]])
B = np.array([[2, 2], [3, 3]])
C = np.array([[3, 3], [2, 2]])
D = np.array([[2, 2], [1, 1]])
E = np.array([[1, 2], [3, 4]])
F = np.array([[2, 3], [1, 4]])
G = np.array([[3, 1], [2, 4]])
H = np.array([[4, 2], [3, 1]])

I = np.vstack((np.hstack((A, B)), np.hstack((C, D))))
J = np.vstack((np.hstack((E, F)), np.hstack((G, H))))
P = np.dot(I, J)

Q11 = np.dot(A, E) + np.dot(B, G)
Q12 = np.dot(A, F) + np.dot(B, H)
Q13 = np.dot(C, E) + np.dot(D, G)
Q14 = np.dot(C, F) + np.dot(D, H)
Q = np.vstack((np.hstack((Q11, Q12)), np.hstack((Q13, Q14))))

print(Q)
print(P)
