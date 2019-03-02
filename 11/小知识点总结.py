
'''
python2 python3: 默认编码2默认ascii，3默认utf-8
python2 print时候不用括号  python3只能加括号
range() xrange()只在2中 生成器
input  2中是raw_input()



=  ==  is：
=是赋值
==是比较值是否相等
is 比较， 比较的是内存地址  id（内容），就是打印出id是多少   print（li1 is li2）
li1 = [1,2,3]
li2 = li1
li3 = li2
print(id(li1),id(li2))


数字，字符串和其他类型

i1 = 6   300
i2 = 6   300
print(id(i1),id(i2))  结果都一样     结果内存不一样
数字和字符串：小数据池，范围之内公用一个，范围大的话就不会共用
数字的范围是-5 --- 256
字符串：1，不能含有特殊字符（不会共用）
        2.s*21以后都是2个地址，20之前都是一个，节省内存

剩下的：list dict tuple set没有小数据池概念
'''