import csv
import matplotlib.pyplot as plt
from datetime import datetime

find = input('輸入欲查詢站名：')
# find = '崎頂'

fn = '每日各站點進出站人數.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    dates, people_in, people_out = [], [], []
    for row in csvReader:
        if row[2] == find:
            dates.append(datetime.strptime(row[0], '%Y%m%d'))
            people_in.append(eval(row[3]))
            people_out.append(eval(row[4]))
        if len(dates) >= 20:
            break

fig = plt.figure(dpi=80, figsize=(9, 6))
plt.plot(dates, people_in, label='in')
plt.plot(dates, people_out, '--', label='out')
plt.legend()
fig.autofmt_xdate()

plt.title(f'台鐵{find}站', fontproperties='Microsoft JhengHei', fontsize=14)
plt.xlabel('2019年', fontproperties='Microsoft JhengHei', fontsize=14)
plt.ylabel('人數', fontproperties='Microsoft JhengHei', fontsize=14)

plt.tick_params(axis='both', labelsize=12, color='red')
plt.show()
