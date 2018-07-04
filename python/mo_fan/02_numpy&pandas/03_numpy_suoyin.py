import numpy as np
A = np.arange(3,15)  #一维
print(A[3])


#二维
A = np.arange(3,15).reshape(3,4)
print(A[2])
print(A[1][1])
print(A[1,1])
print(A[1,1:3])
print(A)
#逐行打印
for row in A:
    print(row)
#逐列打印
for column in A.T:
    print(column)

#迭代输出  矩阵都输出在一行
print(A.flatten())
for item in A.flat:
    print(item)