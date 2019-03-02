s = '金色的蓬莱'
# def my_len():  #函数调用
#     i = 0
#     for k in s:
#         i += 1
#     print(i)

# my_len()

#函数：定义了之后，可以再之后任何需要它的地方调用
#没有返回长度，只是单纯打印

#len（）
#1.不能变，只能计算s字符串的长度
#2.只是输出了结果

#返回的重要性 len（）内置函数

def my_len():  #函数调用
    i = 0
    for k in s:
        i += 1
    print (i)
    return i #返回值return
print(my_len())