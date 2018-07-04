def fun():
#a是局部变量
    a = 10
    print(a)
    return a+100
print(fun())


#全局变量
APPLY = 100 #全局变量
a = None
def fun():
    global a #使用之前在全局里定义的a
    a = 20 #现在的a是全局变量
    return a + 100
print(APPLY)
print('a past:',a)
fun()
print('a now:',a)