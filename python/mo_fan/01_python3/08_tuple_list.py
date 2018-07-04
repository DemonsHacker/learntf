#tuple 用小括号或无括号表述
a_tuple = (12,3,5,15,6)
another_tuple = 12,3,5,15,6
print(a_tuple)

#List 中括号
a_list = [12,3,67,7,82]
print(a_list)

#两者对比
#迭代，输出，运用，定位取值
for content in a_list:
    print(content)
for content_tuple in a_tuple:
    print(content_tuple)

#依次输出a_tuple a_list
for index in range(len(a_list)):
    print("index = ",index,"number in list = ",a_list[index])

for index in range(len(a_tuple)):
    print('index = ',index,'number in tuple = ',a_tuple[index])
