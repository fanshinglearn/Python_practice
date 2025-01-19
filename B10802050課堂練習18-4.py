import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 35, 0.5)
y = np.sin(x / 10)

for i in range(20):
    plt.axis([0, 40, -2, 6])
    plt.scatter(x, y+(i/10), c=x, cmap='rainbow')
plt.show()
