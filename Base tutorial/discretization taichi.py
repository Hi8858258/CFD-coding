import numpy as np
import taichi as ti
from time import time

'''
练习离散方程的基本思路，
求解y' = y - 2x / y 
y(0) = 1
在x范围是1的情况下
(yi+1 - yi)/delta_x = yi - 2xi / yi
yi+1 = yi + (yi - 2xi / yi) * delta_x
'''

ti.init(arch=ti.cpu)
N = 10000
x = np.linspace(0, 1.0, N+1)
y = np.ones(N+1)

@ti.data_oriented
class Solver:
    def __init__(self, Xrange, x, y, N):
        self.Xrange = Xrange
        self.N = N
        self.delta_x = Xrange/N
        self.taichi_x = ti.field(ti.f64, shape = N + 1)
        self.taichi_x.from_numpy(x)
        self.taichi_y = ti.field(ti.f64, shape = N + 1)
        self.taichi_y.from_numpy(y)

    @ti.kernel
    def computer(self):
        self.taichi_y[0] = 1.0
        for i in range(self.N):
            self.taichi_y[i+1] = self.taichi_y[i] + (self.taichi_y[i] - 2 * self.taichi_x[i] / self.taichi_y[i]) * self.delta_x

time_start = time()
t = Solver( Xrange = 1.0, x = x, y = y, N = N)
t.computer()
print(t.taichi_y)
time_end = time()
time_spend = time_end - time_start
print(time_spend)

