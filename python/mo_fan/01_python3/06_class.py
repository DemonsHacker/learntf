
#定义自变量cal等于Calculator
#要加括号"()"
class Calculator1:
    name = 'Good Calculator'
    price = 18
    def add(self,x,y):
        print(self.name)
        result = self.price + x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)


cal = Calculator1()
print(cal.name)
print(cal.price)
cal.add(10,20)


#类init功能
class Calculator:
    name = 'good calculator'
    price = 18
    #下划线是双下划线
    def __init__(self,name,price,height,width,weight):
        self.name = name
        self.price = price
        self.h = height
        self.wi = width
        self.we = weight
c = Calculator('bad calculator',18,17,16,15)
print(c.name)
print(c.price)
print(c.h)
print(c.wi)
print(c.we)