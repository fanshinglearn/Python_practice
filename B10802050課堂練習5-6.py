place = ['觀霧', '日月潭', '阿里山', '小琉球', '墾丁']
print(place)

new_place = input('請輸入新地點:')
place.append(new_place)
print(place)

new_place = input('請輸入新地點:')
place.insert(4, new_place)
print(place)

place.sort()
place.reverse()
print(place)

print(place.index('觀霧'))
place.remove('觀霧')
print(place)

print(place[2], place[4])
del place[2]
del place[4]
print(place)