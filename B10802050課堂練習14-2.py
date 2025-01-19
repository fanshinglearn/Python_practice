import re

msg = '赴酬者聯盟會員輸入聯絡資料，綠巨人好客：02-25525252，米果隊長：(03) 5374281，擂茶索餌：03-4542-542，X同學：037-454545，萬吃王05 575-777，滴嘟人：04-75759475，唉喔面：(06) 5949477，黑剮腹：07-7777477。'

area_num = re.findall(r'0\d', msg)
print(f'由小而大： {sorted(area_num)}')

set_area_num = set(area_num)
print(f'不可重複： {set_area_num}')
