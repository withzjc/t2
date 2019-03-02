#元祖 只读列表，可以被查询不能被更改（儿子不能变，孙子可以变）

# tu = (1,2,3,'alex',[2,3,4,'taibai'],'egon')
# print(tu[3])
# print(tu[0:4])
#
# for i in tu:
#     print(i)
#
# tu[4][3] = tu[4][3].upper()
# print(tu)

#添加
# tu[4][3].append('sb')
# print(tu)

# s = 'alex'
#
# s1 = '_'.join(s)#用什么连接
# print(s1)

# li = ['taibai','alex']
# s=''.join(li)###无缝拼接

###字符串转换成列表就是split    str-------》list
####列表转换成字符串join


#range

# for i in range(0,100,3):
#     print(i)####顾头不顾尾,按顺序排列的数字列表

# for i in range(0,10,-1):###什么都不输出
#     print(i)

li = [1,2,3,5,'alex',[2,3,4,5,'taibai'],'afds']

for i in range(len(li)):
    if type(li[i]) == list:
        for j in li[i]:
            print(j)
    else:print(li[i])