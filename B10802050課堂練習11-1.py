def openfile(fn):
    with open(fn, encoding="utf-8") as file_Obj:
        list1 = []
        for line in file_Obj:
            list1.append(line)
        print(list1)

        list2 = []
        for line in list1:
            list2.append(line.rstrip())
        return list2

fn = 'B10802050課堂練習11-1.txt'
list2 = openfile(fn)
print(list2)

list3 = list2
list3.sort()
print(list3)
