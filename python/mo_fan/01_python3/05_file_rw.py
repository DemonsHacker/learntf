#\n换行命令  查看使用\n和不适用\n的区别
text = 'this is my first test.this is the second line.this the third'
print(text)

print('\n')

text='this is my first test.\nThis is the second line.\nthis the third line'
print(text)

#open 读文件方式
#以写的方式打开文件
my_file = open('my file.txt','w')
my_file.write(text)
my_file.close()#关闭文件

#\t tab对齐
text = '\tThis is my first test.\n\tThis is the second line.\n\tThis is the third line'
print(text)


#读写文件  给文件增加内容
append_text = '\nThis is appended file'
#以增加内容的形式打开
my_file = open('my file.txt','a')
my_file.write(append_text)
my_file.close()


#读取文件内容 file.read()
file = open('my file.txt','r')
content = file.read()#读取文本的所有内容
print(content)

print()

#按行读取 file.readline()
file = open('my file.txt','r')
content = file.readline() #读取第一行
print(content)

#读取第二行
second_read_time = file.readline()
print(second_read_time)