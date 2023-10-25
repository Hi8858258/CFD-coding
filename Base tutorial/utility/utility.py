from time import time
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#time装饰
def timer(func):
    def func_wrapper(*args, **kwarge):
        time_start = time()
        result = func(*args, **kwarge)
        time_end = time()
        time_spend = time_end - time_start
        print('\n{0} cost time {1} s\n'.format(func.__name__, time_spend))
        return result
    return func_wrapper

#得到2D结构笛卡尔网格的体心坐标
def get_position(nx, ny, deltax, deltay):
    
    cell = np.ones([nx * ny,2])
    for i in range(len(cell)):
        # #先获取每个网格的局部位置，比如左下角网格的位置就是（0，0），右上角就是（nx-1,ny-1）
        x_position = i % nx
        y_position = i // nx
        # #再通过网格的位置计算出每个网格体心的坐标
        cell[i,0] = deltax/2 + deltax * x_position
        cell[i,1] = deltay/2 + deltay * y_position
    return cell

#画云图
def plot_contour (Coordx, Coordy, T, minX, maxX, minY, maxY):

    X = np.linspace(minX, maxX, 3)
    Y = np.linspace(minY, maxY, 4)
    #生成二维数据坐标点
    X1, Y1 = np.meshgrid(X,Y)
    print(X1)
    print(Y1)

    Z = interpolate.griddata((Coordx, Coordy), T, (X1,Y1), method='cubic')

    fig, ax = plt.subplots(figsize = (6,8))

    levels = range((int)(T.min()),(int)(T.max()+10),5)

    cset1 = ax.contourf(X1,Y1,Z,levels,cmap = cm.jet)
    ax.set_xlim(minX, maxX)
    ax.set_ylim(minY, maxY)
    ax.set_xlabel("X(mm)", size = 15)
    ax.set_ylabel("Y(mm)", size = 15)
    
    cbar = fig.colorbar(cset1)
    cbar.set_label('T', size =18)

    plt.show()