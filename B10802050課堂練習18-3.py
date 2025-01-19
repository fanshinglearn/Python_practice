import matplotlib.pyplot as plt
import random

x = 0
y = 0
for i in range(10):
    plt.clf()
    plt.axis([-10, 10, -10, 10])
    plt.scatter(x, y)
    plt.legend([f'({x}, {y})'])
    plt.pause(0.5)
    x += random.randint(-1, 1)
    y += random.randint(-1, 1)
plt.show()