# fruits = {'西瓜' : [20, 500], '香蕉' : [18, 200], '水蜜桃' : [55, 200], '蘋果' : [25, 300]}
fruits = {}
inp = True

while inp:
    fruit = input('\n請輸入水果 : ')
    money = int(input('一斤多少錢 : '))
    catty = int(input('進多少斤 : '))

    fruits[fruit] = [money, catty]
    repeat = input('是否要繼續輸入 ? (y/n) ')
    if repeat != 'y':
        inp = False

print()

for fruit, num in fruits.items():
    print('水果名稱 : %s ，單價(元) : %d ，數量(斤) : %d 。'%(fruit, num[0], num[1]))