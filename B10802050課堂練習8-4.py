def club_member(name, age, hobby_list):
    member_dict = {'Name':name, 'Age':age}
    for hobby in hobby_list:
        member_dict['嗜好%d'%hobby_list.index(hobby)] = hobby
    return member_dict

name = input('姓名 : ')
age = input('年齡 : ')
hobby_list = []
while True:
    hobby = input('嗜好 : ')
    if hobby != 'n':
        hobby_list.append(hobby)
    else:
        break
member = club_member(name, age, hobby_list)
print(member)

