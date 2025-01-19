import matplotlib.pyplot as plt
import numpy as np

# t = [0.000, 0.524, 1.047, 1.571, 2.094, 2.618, 3.142, 3.665, 4.189, 4.712, 5.236, 5.760, 6.283]
t = np.round(np.linspace(0, 6.283, 13),3)
f1 = [0, 0.5, 0.875, 1, 0.875, 0.5, 0, -0.5, -0.875, -1, -0.875, -0.5, 0]
f2 = [1, 0.875, 0.5, 0, -0.5, -0.875, -1, -0.875, -0.5, 0, 0.5, 0.875, 1]

plt.xticks(t)
plt.plot(t, f1, '-', t, f2, '--')
plt.title("sint'-' vs cost'--'", fontsize=20)
plt.xlabel('t', fontsize=20)
plt.ylabel('f(t)', fontsize=20)
plt.show()
