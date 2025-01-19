def read_file(fn):
    with open(fn, encoding='utf-8') as file_Obj:
        print(file_Obj.read())

str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'
practice1 = 'B10802050課堂練習11-3-1.txt'
practice2 = 'B10802050課堂練習11-3-2.txt'
practice3 = 'B10802050課堂練習11-3-3.txt'
practice4 = 'B10802050課堂練習11-3-4.txt'

# 1
with open(practice1, 'w', encoding='utf-8') as file_Obj:
    file_Obj.write(str1)
    file_Obj.write(str2)
read_file(practice1)

# 2
with open(practice2, 'w', encoding='utf-8') as file_Obj:
    file_Obj.writelines(str1)
    file_Obj.writelines(str2)
read_file(practice2)

# 3
str_list = [str1, str2]
with open(practice3, 'w', encoding='utf-8') as file_Obj:
    file_Obj.writelines(str_list)
read_file(practice3)

# 4
# input_str1 = 'I love Python.'
input_str1 = input('請輸入字串一：')
with open(practice4, 'w', encoding='utf-8') as file_Obj:
    file_Obj.write(input_str1)
read_file(practice4)

# input_str2 = 'Learn Python from the best book.'
input_str2 = input('請輸入字串二：')
with open(practice4, 'a', encoding='utf-8') as file_Obj:
    file_Obj.write(input_str2)
read_file(practice4)
