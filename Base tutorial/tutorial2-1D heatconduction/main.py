import numpy as np
import matplotlib.pyplot as plt

'''
将控制方程通过FVM离散成代数方程
(Tl-Tc)/deltax + (Tr-Tc)/deltax = 0

'''

s = 1
L = 0.5 #unit是m
n = 100
deltax = L/n
Area = 0.01 #unit是m2
k = 1000 #unit是1000/（w*m）

#左右边界温度℃
T_left = 100
T_right = 500

#系数矩阵初始化
A = np.zeros((n,n))
X = np.zeros((n))
B = np.zeros((n))

g = k * Area /deltax
for i in range(n):
    if i == 0:
        a_cell = -3 * g
        a_left = 0
        a_right = g  
        b = -2 * g * T_left
        A[i, i] = a_cell
        A[i, i+1] = a_right
        B[i] = b

    elif i == n-1:
        a_cell = -3 * g
        a_left = g
        a_right = 0
        b = -2 * g * T_right
        A[i, i] = a_cell
        A[i, i-1] = a_left
        B[i] = b
    else:
        a_cell = -2 * g
        a_left = g
        a_right = g
        A[i, i] = a_cell
        A[i, i - 1] = a_left
        A[i, i + 1] = a_right
X = np.linalg.solve(A,B)

#print(X)

x_axis= np.linspace(deltax/2, L-deltax/2, n)
y_accurate = 800 * x_axis + 100
print(x_axis)
print(y_accurate)
print(X)
#精确解
#plt.figure(figsize=(8,8))
plt.scatter(x_axis, y_accurate)
plt.plot(x_axis, X, color = 'red')
plt.show()
        