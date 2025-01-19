import matplotlib.pyplot as plt
import numpy as np

color = ['red', 'green', 'blue']

for i in range(3):
    x = [0, 1, 2, 3]
    y = np.random.rand(4)
    plt.subplot(3, 1, i+1)
    plt.axis([-0.5, 3.5, 0, 1])
    plt.xticks(x)
    plt.yticks(np.arange(0, 1.2, 0.2))
    plt.bar(x, y, 0.35, color=color[i], label=f'row{i+1}')
    plt.legend()

plt.show()
