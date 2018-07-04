
'''
    属性：（维度）ndim，（行数和列数）shape，(元素个数）size
'''
import numpy as np
array = np.array([[1,2,3],[2,3,4]])
print(array)

#维度
print('number of dim:',array.ndim)
#行数和列数
print('shape:',array.shape)
#大小
print('size:',array.size)

'''array的创建
array 创建数组
dtype 指定数据类型
zeros 创建数据全为0
ones 创建数据全为1
empty 创建数据接近0
arrange 按指定范围创建数据
linspace 创建线段
'''
a = np.array([2,23,4])
print(a)

# ---- 指定dtype
a = np.array([2,23,4],dtype=np.int)
print(a.dtype)
a = np.array([2,23,4],dtype=np.int32)
print(a.dtype)
a = np.array([2,23,4],dtype=np.float)
print(a.dtype)
a = np.array([2,23,4],dtype=np.float32)
print(a.dtype)

# ----  创建特定数据
a = np.array([[2,23,4],[2,32,4]])
print(a)

a = np.zeros((3,4))  #全零数组
print(a)

a = np.ones((3,4),dtype=np.int) #全一数组
print(a)

a = np.empty((3,4),dtype=np.float)
print(a)

#用arange创建连续数组  10-19 步长2
a = np.arange(10,20,2)
print(a)

#使用reshape改变数据的形状
a = np.arange(12).reshape((3,4))
print(a)

#使用linspace创建线段型数据
#开始端1 结束端10  且分割成20个数据  生成线段
a = np.linspace(1,10,20)
a = np.linspace(1,10,20).reshape((5,4))





