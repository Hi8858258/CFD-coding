import numpy as np
from time import time
import matplotlib.pyplot as plt

'''
练习离散方程的基本思路，
求解y' = y - 2x / y 
y(0) = 1
在x范围是1的情况下
(yi+1 - yi)/delta_x = yi - 2xi / yi
yi+1 = yi + (yi - 2xi / yi) * delta_x
'''

time_start = time()
range_x = 1.0
N = 100 #先将求解域离散成N等分
x, delta_x = np.linspace(0.0, 1.0, N + 1, retstep= True)
y = np.ones(N+1, dtype=np.float64)

def result(N, x, y, delta_x):
    for i in range(N):
        y[i+1] = y[i] + (y[i] - 2 * x[i] / y[i]) * delta_x
    return y

t = result(N, x, y, delta_x)
time_end = time()
print(t)
time_spend = time_end - time_start
print(time_spend)

y_real = np.sqrt(1 + 2 * x)
print (y_real)

plt.figure(figsize = (5, 5))

plt.scatter(x, y)
plt.plot(x, y_real, color = 'red')


plt.show()
