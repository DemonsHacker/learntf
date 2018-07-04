#打印0-9的所有数据
condition = 0
while condition < 10:
    print(condition)
    condition = condition + 1

a = range(10)
while a:
    print(a[-1])
    a = a[:len(a)-1]  #使用切片去掉最后一个元素