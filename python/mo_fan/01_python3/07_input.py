a_input = input('please input a number:')
print('this is number is:',a_input)

b = int(input('please input a number:'))
if b == 1:
    print('this is a good one')
elif b == 2:
    print('see you next time')
else:
    print('Good luck')

#input扩展
score = int(input('Please input your score:\n'))
if score>=90:
    print('Congradulationm,you get an A')
elif score >=80:
    print('You get a B')
elif score >=70:
    print('You get a C')
elif score >=60:
    print('You get a D')
else:
    print('Sorry,You are failed')