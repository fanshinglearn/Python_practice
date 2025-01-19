import time
xtime = time.localtime()

def day(hour):
    if hour >= 24:
        return hour - 24
    elif hour < 0:
        return hour + 24
    else:
        return hour

print('台灣 : %d 點 %d 分 %d 秒'%(xtime.tm_hour, xtime.tm_min, xtime.tm_sec))
print('東京 : %d 點 %d 分 %d 秒'%(day(xtime.tm_hour + 9 - 8), xtime.tm_min, xtime.tm_sec))
print('巴黎 : %d 點 %d 分 %d 秒'%(day(xtime.tm_hour + 2 - 8), xtime.tm_min, xtime.tm_sec))
print('倫敦 : %d 點 %d 分 %d 秒'%(day(xtime.tm_hour + 1 - 8), xtime.tm_min, xtime.tm_sec))
print('紐約 : %d 點 %d 分 %d 秒'%(day(xtime.tm_hour - 5 + 8), xtime.tm_min, xtime.tm_sec))
print('夏威夷 : %d 點 %d 分 %d 秒'%(day(xtime.tm_hour - 12 + 8), xtime.tm_min, xtime.tm_sec))