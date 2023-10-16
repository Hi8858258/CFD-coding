import numpy as np
import matplotlib.pyplot as plt

'''
一维常系数对流方程
'''

n = 41
xrange = 2
x, dx = np.linspace(0, xrange, n, retstep=True)
dt = 0.025
nt = 25
c = 1 #常数
#print (x, dx)

#指定初始条件，制造一个初始的方波
u = np.ones(n)
u[int(0.5/dx): int(1/dx + 1)] = 2

plt.figure(figsize=(5,4))
plt.plot(x, u, color = 'red', label = 'init')

for i in range(nt):
    un = u.copy()
    for i in range(1, n):
        u[i] = un[i] - c* dt / dx * (un[i] - un[i-1])

plt.plot(x, u, color = 'blue', label = 'new')
plt.show()