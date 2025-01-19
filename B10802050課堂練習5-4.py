list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []
list3 = []

for i in range(len(list1)):
    popped_list1 = list1.pop()
    print(popped_list1)
    list2.insert(10,popped_list1)
    print(list2)

print()

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10):
    if i % 2 == 1:
        print(i)
        list1.remove(i)
        print(list1)

print()

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10):
    if list1[i] > 6:
        list3.insert(10,list1[i])
        print(list3)