import matplotlib.pyplot as plt
import numpy as np

t = np.round(np.linspace(0, 6.283, 13),3)
f1 = [0, 0.5, 0.875, 1, 0.875, 0.5, 0, -0.5, -0.875, -1, -0.875, -0.5, 0]
f2 = [1, 0.875, 0.5, 0, -0.5, -0.875, -1, -0.875, -0.5, 0, 0.5, 0.875, 1]

plt.xticks(t)
lineA, = plt.plot(t, f1, 'g-', label='sint')
lineB, = plt.plot(t, f2, 'r--', label='cost')
plt.legend(handles=[lineA, lineB], loc=9)
plt.title('正弦sint vs 餘弦cost', fontproperties='Microsoft JhengHei', fontsize=20)
plt.xlabel('角度(經度量)', fontproperties='Microsoft JhengHei', fontsize=20)
plt.ylabel('函數值', fontproperties='Microsoft JhengHei', fontsize=20)
plt.savefig('B10802050課堂練習18-2.jpg', bbox_inches='tight')
plt.show()
