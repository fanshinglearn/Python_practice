fruits = {}
x = True

while x:
    fruit = input('\n請輸入水果:')
    money = input('一斤多少錢:')
    catty = input('進多少斤:')
    fruits[fruit] = [int(money), int(catty)]
    repeat = input('是否要繼續輸入? (y/n)')
    if repeat != 'y':
        x = False

for fruit, i in fruits.items():
    print('水果名稱:%s，單價(元):%d，數量(斤):%d。'%(fruit, i[0], i[1]))