import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime
import numpy as np

內灣線 = ['北新竹', '千甲', '新莊', '六家', '竹中', '上員', '竹東', '橫山', '九讚頭', '合興', '富貴', '內灣']

fn = '每日各站點進出站人數.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    dates, daily_sum = [], []

    sum = 0

    for row in csvReader:
        if row[2] in 內灣線:
            if row[0] not in dates:
                if dates != []:
                    daily_sum.append(sum)
                if len(dates) >= 20:
                    break
                else:
                    sum = 0
                    dates.append(datetime.strptime(row[0], '%Y%m%d'))
            sum += int(row[3]) + int(row[4])

# print(內灣線)
# print(len(內灣線))
# print(dates)
# print(len(dates))
# print(daily_sum)
# print(len(daily_sum))


# ax = plt.axes(projection='3d')
# ax.plot3D(x,y,z)

fig = plt.figure()
ax = Axes3D(fig)
x = np.array(內灣線)
y = np.array(dates)
z = np.array(daily_sum)

ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap = 'rainbow')
ax.set_title("3D曲面圖", fontproperties="SimSun")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
