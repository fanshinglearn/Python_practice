def build_vip(id, name, tel = ""):
    vip_dict = {'VIP_ID':id, 'Name':name}
    if tel:
        vip_dict['Tel'] = tel
    return vip_dict

member_list = []
repeat = 'y'
while repeat == 'y':
    id = input('id : ')
    name = input('name : ')
    tel = input('tel : ')
    member = build_vip(id, name, tel)
    member_list.append(member)
    print('最新成員資料 : %s'%member_list)
    repeat = input('是否要繼續輸入會員資料? (y/n)')

print(member_list)
for member in member_list:
    print(member)
