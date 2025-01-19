import math

x0 = math.sqrt((4-(4*(-8))))
x1 = lambda x:(2+x)/2
x2 = lambda x:(2-x)/2

print("兩根為:",x1(x0),x2(x0))

List = []
for x in range(-5,6):
     A = lambda x:((x)-(2*x))-8
     List.append(A(x))

print("最大:",List.index(max(List))-5)
print("最小:",List.index(min(List))-5)