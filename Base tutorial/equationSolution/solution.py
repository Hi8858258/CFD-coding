import numpy as np 

def Gauss_elimination(A, B):
    
    row, column = A.shape
    X = np.zeros(row)
    #构造上三角矩阵
    for i in range(row): 
        for j in range(i+1, row):

            ration = A[j,i] / A[i,i] #后续需要考虑到当A[i,i]为0的情况
            A[j] = A[j] - A[i] * ration
            B[j] = B[j] - B[i] * ration

    #返回求解
    for i in range(row-1, -1, -1):
        if i == row - 1:
            X[i] = B[i]/A[i,i]
        else:
            for j in range(column-1, i , -1):
                B[i] = B[i] - X[j] * A[i, j]
            X[i] = B[i] / A[i,i]

    return(X)

def Jacobi(A, b, error, step):
    '''
    用雅可比迭代计算矩阵方程,主要是构建出A = D + L + U
    '''
    n = A.shape[1]
    X_old = np.zeros(n, dtype=np.float64)
    X_new = np.zeros(n, dtype=np.float64)
    D = np.zeros((n, n), dtype=np.float64)
    D_inverse = np.zeros((n, n), dtype=np.float64)
    #获得D和其逆矩阵
    for i in range(n):
        D[i,i] = A[i,i]
        D_inverse[i,i] = 1 / A[i,i]
    #获得L+U矩阵
    LU = A - D

    for i in range(1,step):
        X_new = np.dot(D_inverse,b) - np.dot(D_inverse, np.dot(LU, X_old))
        if np.max(np.abs(X_new - X_old)) <= error:
            return(X_new)
        X_old = X_new
    
    return(X_new)

def Gauss_seidel(A,b,error,step):
    '''
    高斯赛德尔迭代, 要分别获得D对角矩阵, L下三角矩阵, U上三角矩阵
    '''
    n = A.shape[1]
    D = np.zeros((n, n), dtype=np.float64)
    L = np.zeros((n, n), dtype=np.float64)
    U = np.zeros((n, n), dtype=np.float64)
    X_old = np.zeros(n, dtype=np.float64)
    X_new = np.zeros(n, dtype=np.float64)
    #获得D和其逆矩阵
    for i in range(n):
        D[i,i] = A[i,i]
    
    #获得L下三角矩阵
    for i in range(n):
        for j in range(n):
            if i > j:
                L[i,j] = A[i,j]
    #获得上三角举证
    U = A - D - L

    DL_inverse = np.linalg.inv(D+L)

    for i in range(1,step):
        X_new = np.dot(DL_inverse,b) - np.dot(DL_inverse, np.dot(U, X_old))
        if np.max(np.abs(X_new - X_old)) <= error:
            return(X_new)
        X_old = X_new
    
    return(X_new)





A_list = [[3, -1, 0, 0],
        [-2, 6, -1, 0],
        [0, -2, 6, -1],
        [0, 0, -2, 7]]
b_list = [3,4,5,-3]
A = np.array(A_list, dtype=np.float64)
b = np.array(b_list, dtype=np.float64)

a = Gauss_seidel(A, b, 0.005, 1000)
print(a)

result = np.dot(A, a)
print(result)
    


# A_list = [[2,-1,3,2],
#           [3,-3,3,2],
#           [3,-1,-1,2],
#           [3,-1,3,-1]]

# A = np.array(A_list, dtype=np.float64)
# B = np.array([6,5,3,4], dtype=np.float64)

# a = Gauss_elimination(A,B)
# print(a)


