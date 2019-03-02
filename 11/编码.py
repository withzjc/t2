'''
ascii码:没有中文，一个字符一个字节
    A：00000010一个字节八位
unicode：开始16位后来32位
    A：32位
    中：32位四个字节
utf-8
    A：8位 0010 0000
    中：24位3个字节
gbk
    A：8位一个字节
    中：16位2个字节

1.各个编码之间的二进制，是不能互相识别的，会产生乱码。。
2。Unicode容量太大，文件储存传输都是gbk和utf-8


py3：str在内存中是用Unicode编码的。
    bytes类型 是特殊的，不是用Unicode编码的，传输和存储过程要转换成bytes类型
    对于英文：
        str：表现形式 s ='alex'，，内部存储编码方式 Unicode的010101010
        bytes：表现形式 s = b'alex'
                编码方式： 00101010 utf-8 gbk。。。。

    对于中文： bytes类型不一样了 s =b'x\e91\e91\e01\e21\e32'是十六进制  utf-8 gbk


    str转换成bytes

'''

s1 = 'alex'
#encode如何将str-》bytes  编码
s11 = s1.encode('utf-8')
print(s11)

s2 = '中国'
s22 = s2.encode('gbk')
print(s22)