import numpy as np

'''
对一维矩阵进行操作
'''
a = np.array([10,20,30,40])
b = np.arange(4)
print(a)
print(b)

#基本运算   即矩阵运算
c = a - b
print(c)
c = a + b
print(c)
c = a * b
print(c)

#矩阵的幂
c = b**2
print(c)

#数学函数
c = 10*np.sin(a)
print(c)
print(b)
print(b<3)  #每个元素都与3比较

'''
对多维矩阵操作
'''
a = np.array([[1,1],[0,1]])
b = np.arange(4).reshape((2,2))
print(a)
print(b)

#矩阵乘法  对应元素相乘  和  矩阵乘法
c_dot = np.dot(a,b)  #矩阵乘法
c_dot_2 = a.dot(b)   #同上
print(c_dot)
print(c_dot_2)

a = np.random.random((2,4))
print(a)

print(np.sum(a))
print(np.min(a))
print(np.max(a))

#查找运算  对行和列  对axis赋值
print("a = ",a)
#axis=0以列为查找单元
print("sum = ",np.min(a,axis=1))
#axis=1以行为查找单元

A = np.arange(2,14).reshape((3,4))
print(np.argmax(A)) #矩阵A中元素最大的下标
print(np.argmin(A)) #矩阵A中元素最小的下标

#均值
print(np.mean(A))
print(np.average(A))

#求均值 另一种写法
print(A.mean())   #求均值
print(A)

#cumsum()生成的矩阵中序号为n
#是原矩阵中从0到n的和
print(np.cumsum(A))
print(A)
#累差运算  每一行中后一项与前一项的差
print(np.diff(A))

#将所有非零元素的行和列坐标分割开  重构成两个分别关于行和列的矩阵
print(np.nonzero(A))

#排序操作
A = np.arange(14,2,-1).reshape((3,4))
print(np.sort(A))

#矩阵的转置
print(np.transpose(A))
print(A.T)

#clip(Array,Array_min,Array_max)
#判断矩阵中元素是否比最小值小  或者比最大值大
#满足则转换为最小值  或者  最大值
print(A)
print(np.clip(A,5,9))