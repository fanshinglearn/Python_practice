fruits1 = {'西瓜':20, '香蕉':18, '水蜜桃':55, '蘋果':25}
fruits2 = dict({'西瓜':20, '香蕉':18, '水蜜桃':55, '蘋果':25})
fruits3 = dict(zip(['西瓜', '香蕉', '水蜜桃', '蘋果'], [20, 18, 55, 25]))

print(fruits1)
print(fruits2)
print(fruits3)

fruit = input('輸入水果名稱 : ')
if fruit in fruits1:
    print('%s一斤%d元'%(fruit, fruits1[fruit]))
else:
    print('抱歉!沒有販賣~%s~這種水果'%fruit)