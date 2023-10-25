# import sys
# import os
# sys.path.append(os.getcwd())

import numpy as np
import matplotlib.pyplot as plt
from utility import utility
from equationSolution import solution

#input value
L_x = 0.3 #unit m
L_y = 0.4 #unit m
k = 1000 #unit W/m.k
q = 500 #unit kw/m2
T_top = 100 # unit ℃

#discretization space
nx = 3
ny = 4
deltax = L_x/nx
deltay = L_y/ny

'''
control equation
a c*Phi c + a w *Phi w + a e * Phi e + a n *Phi n + a s *Phi s = 0
a c = (2*k*deltay/deltax + 2*k*deltax/deltay)
a w = -k * deltay/deltax
a e = -k * deltay/deltax
a n = -k * deltax/deltay
a s = -k * deltax/deltay
'''

n = nx * ny

#组建系数举证
A = np.zeros((n,n))
B = np.zeros(n)
T = np.zeros(n)

g_horizontal = k * deltay / deltax
g_vertical = k * deltax / deltay

for i in range(n):
    #South 边界
    if i // nx == 0:
        #左下角
        if i == 0:
            a_west = 0
            a_east = - g_horizontal
            a_north = - g_vertical
            a_south = 0
            a_cell = a_east + a_west + a_north + a_south
            b = 500 * 1000 * deltay
            A[i, i] = -a_cell
            A[i, i + 1] = a_east
            A[i, i + nx] = a_north
            B[i] = b

        #右下角
        elif i == nx-1:
            a_west = - g_horizontal
            a_east = 0
            a_north = -g_vertical
            a_south = 0
            a_cell = a_east + a_west + a_north + a_south
            b = 0
            A[i, i] = -a_cell
            A[i, i - 1] = a_west
            A[i, i + nx] = a_north
            B[i] = b
        #第一行中间的网格
        else:
            a_west = - g_horizontal
            a_east = -g_horizontal
            a_north = -g_vertical
            a_south = 0
            a_cell = a_east + a_west + a_north + a_south
            b = 0
            A[i, i] = -a_cell
            A[i, i - 1] = a_west
            A[i, i + 1] = a_east
            A[i, i + nx] = a_north
            B[i] = b
    
    #North边网格
    elif i // nx == ny - 1:
        #左上角网格
        if i == nx * (ny - 1):
            a_west = 0
            a_east = -g_horizontal
            a_north = -2 * g_vertical
            a_south = -g_vertical
            a_cell = a_east + a_west + a_north + a_south
            b = 500 * 1000 * deltay + 2 * k* deltax / deltay * (T_top + 273.15)
            A[i, i] = -a_cell
            A[i, i + 1] = a_east
            A[i, i - nx] = a_south
            B[i] = b
        #右上角网格
        elif i == nx * ny -1:
            a_west = - g_horizontal
            a_east = 0
            a_north = -2 * g_vertical
            a_south = -g_vertical
            a_cell = a_east + a_west + a_north + a_south
            b = 2 * g_vertical * (T_top + 273.15)
            A[i, i] = -a_cell
            A[i, i - 1] = a_west
            A[i, i - nx] = a_south
            B[i] = b
        #中间网格
        else:
            a_west = - g_horizontal
            a_east = - g_horizontal
            a_north = -2 * g_vertical
            a_south = -g_vertical
            a_cell = a_east + a_west + a_north + a_south
            b = 2 * g_vertical * (T_top + 273.15)
            A[i, i] = -a_cell
            A[i, i + 1] = a_east
            A[i, i - 1] = a_west
            A[i, i - nx] = a_south
            B[i] = b
   #west网格
    elif i % nx == 0:
        if i != 0 or i != nx * (ny - 1):
            a_west = 0
            a_east = - g_horizontal
            a_north = -g_vertical
            a_south = -g_vertical
            a_cell = a_east + a_west + a_north + a_south
            b = 500 * 1000 * deltay
            A[i, i] = -a_cell
            A[i, i + 1] = a_east
            A[i, i - nx] = a_south
            A[i, i + nx] = a_north
            B[i] = b

    #east边界其余网格
    elif (i+1) % nx == 0:
        if i != nx or i != nx*ny - 1:
            a_west = - g_horizontal
            a_east = 0
            a_north = -g_vertical
            a_south = -g_vertical
            a_cell = a_east + a_west + a_north + a_south
            b = 0
            A[i, i] = -a_cell
            A[i, i - 1] = a_west
            A[i, i + nx] = a_north
            A[i, i - nx] = a_south
            B[i] = b
    #中间网格
    else:
        a_west = - g_horizontal
        a_east = - g_horizontal
        a_north = -g_vertical
        a_south = -g_vertical
        a_cell = a_east + a_west + a_north + a_south
        b = 0
        A[i, i] = -a_cell
        A[i, i - 1] = a_west
        A[i, i + 1] = a_east
        A[i, i + nx] = a_north
        A[i, i - nx] = a_south
        B[i] = b

T = np.linalg.solve(A,B)
#T = solution.Gauss_elimination(A,B)
#T = solution.Jacobi(A, B, 0.005, 1000)
#T = solution.Gauss_seidel(A, B, 0.005, 1000)
T_new = T - 273.15
print(T_new)

cell = utility.get_position(nx, ny, deltax, deltay)

Coordx = cell[:,0]
Coordy = cell[:,1]
#print (Coordx, Coordy)

fdf = utility.plot_contour(Coordx, Coordy, T_new, 0, L_x, 0, L_y)

 