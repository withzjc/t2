#Naruto.txt


#1.文件路径  编码方式：utf-8 GBK
# 以什么方式打开：只读  只写 追加 读写 写读。。。。

# f = open('1.txt',mode='r',encoding='utf-8')
# content = f.read()
# print(content)
# f.close()

#只读：r  rb
#只写：w  先将源文件的内容全部清除在写
#wb写（没有编码方式，用的啥就是啥）

#追加a
#读写 r+,先读后写，，，写读的话读是从光标占得位置
#f = open('1.txt',mode='r+',encoding='utf-8')
#print(f.read())
#f.write('22')
#print(f.read())
#f.close()   ropen里面只要有b就不用encoding
#f.seek(0)调光标，，，按照字节定光标


#功能详解
#f.tell()告诉光标位置，然后再进行seek  seek（count-i） f.read(2)
#f.readale()是否可读
#f.readline（）一行一行的读 f.readlines() 每一行当成列表中的一个元素，添加到列表中，可以循环打印出来
#f.trumcate()截取一段读出来，截取前几位 对源文件操作


#with  open('1.txt',mode='r',encoding='')as obj，open...可以同时打开2个
#   obj.read()  #自动关闭

usrname = input('请输入你的名字：')
password = input('请输入你的密码：')

with open('list_of_info',mode='w',encoding='utf-8')as f:
    f.write('{}\n{}'.format(usrname,password))
print('恭喜你，注册成功！')

i=0

while i <3:
    uname = input('请输入名字：')
    upass = input('请输入密码：')
