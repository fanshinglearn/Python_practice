# A = {1, 2, 3, 4}
# B = {4, 5, 6, 7}
# C = {7, 8, 9, 0}

A = set(input('集合A : '))
B = set(input('集合B : '))
C = set(input('集合C : '))

boolean = A.isdisjoint(B)
if boolean == True:
    boolean = False
else:
    boolean = True
print('A和B有共同元素是', boolean)

AUB = A.union(B)
print('AUB = ', A.union(B))
print('(AUB)∩C = ', A.union(B).intersection(C))
print('(A∩C)U(B∩C) = ', A.intersection(C).union(B.intersection(C)))
print('(AUB)∩C與(A∩C)U(B∩C)相等是', A.union(B).intersection(C) == A.intersection(C).union(B.intersection(C)))