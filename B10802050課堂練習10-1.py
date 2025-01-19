from order import order

appetizer = ['開胃菜', '凱薩沙拉', '鮮蝦蘆筍', '水果沙拉']
soup = ['湯品', '香菇雞肉湯', '鮮魚湯', '牛肉湯']
course = ['主菜', '超級厚黑牛排', '夭壽鮮嫩魚排', '不好吃砍頭雞排']
dessert = ['甜點', '法式布蕾', '炭烤布丁', '橙汁奶酪']

menu = []
menu.append(order(appetizer))
menu.append(order(soup))
menu.append(order(course))
menu.append(order(dessert))
print('你點的菜單為 %s : %s，%s : %s，%s : %s，%s : %s'%(appetizer[0], appetizer[menu[0]],
                                                        soup[0], soup[menu[1]],
                                                        course[0], course[menu[2]],
                                                        dessert[0], dessert[menu[3]]))
