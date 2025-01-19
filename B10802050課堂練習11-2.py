fn = 'B10802050課堂練習11-2.txt'
with open(fn, encoding='utf-8') as file_Obj:
    list_data = file_Obj.readlines()
print(list_data)

str_data = ''
for line in list_data:
    str_data += line
print(str_data)

str_data = str_data.replace('能', '想')
print(str_data)

str_data = str_data.replace('喜歡', '想要')
print(str_data)

# findstr_A = '穿'
# findstr_B = '露'
findstr_A = input('請輸入欲搜尋字串A：')
findstr_B = input('請輸入欲搜尋字串B：')

print(f'A在字串中出現的次數：{str_data.count(findstr_A)}')
print(f'A第一次出現在字串的位置：{str_data.find(findstr_A)}')

str_data = str_data.replace(findstr_A, findstr_B)
print(str_data)
