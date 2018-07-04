#def 函数
def function():
    print('this is a function')
    a = 1+2
    print(a)


function()  #调用函数

#函数参数
def func(a,b):
    c = a+b
    print('the %i is %i + %i' %(c,a,b))

func(2,3)

#函数默认参数
def sale_car(price,color='red',brand='carmy',is_second_hand=True):
    print('price',price,
          'color',color,
          'brand',brand,
          'is_second_hand',is_second_hand)

sale_car(17,brand='car')

#单元测试  执行脚本的时候执行这些代码
'''
if _name_=='_main_':
    #code_here
'''

#可变参数
'''
可变参数在函数定义不能出现在
特定参数和默认参数前面

可变参数grades前有*修饰，表明
该参数是一个可变参数，是一个可
迭代的对象
'''
def report(name,*grades):
    total_grade = 0
    for grade in grades:
        total_grade += grade
    print(name,'total grade is',total_grade)
report('LanZe',8,9,10,15)

#关键字参数
'''
可传入0个或者任意个含有参数名的
参数，这些参数名在函数定义中并没
有出现，这些参数在函数内部自动封
装成一个字典dict



关键字参数  使用**修饰
通常关键字参数放在函数参数列表的最后
'''
def portrait(name,**kw):
    print('name is',name)
    for k,v in kw.items():
        print(k,v)

portrait('Mike',age=24,country='China',education='bachelor')