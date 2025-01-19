import numpy as np

A = np.random.randn(5000)

print(np.mean(A))
print(np.std(A))
print(f'[-3, -2.4)\t: {((A >= -3) & (A < -2.4)).sum()}')
print(f'[-2.4, -1.8)\t: {((A >= -2.4) & (A < -1.8)).sum()}')
print(f'[-1.8, -1.2)\t: {((A >= -1.8) & (A < -1.2)).sum()}')
print(f'[-1.2, -0.6)\t: {((A >= -1.2) & (A < -0.6)).sum()}')
print(f'[-0.6, 0)\t: {((A >= -0.6) & (A < 0)).sum()}')
print(f'[0, 0.6)\t: {((A >= 0) & (A < 0.6)).sum()}')
print(f'[-0.6, 1.2)\t: {((A >= 0.6) & (A < 1.2)).sum()}')
print(f'[1.2, 1.8)\t: {((A >= 1.2) & (A < 1.8)).sum()}')
print(f'[1.8, 2.4)\t: {((A >= 1.8) & (A < 2.4)).sum()}')
print(f'[2.4, 3)\t: {((A >= 2.4) & (A < 3)).sum()}')
