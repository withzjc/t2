#字典（映射数据类型，一个键对应一个数值）

#数据类型划分：可变数据类型   不可变数据类型

#不可变数据类型：元组  bool值  int str (可hash)

#可变数据类型： 列表list  字典dict   set（本身可变，中的元素不可变）不可hash

#dict key必须是不可变数据类型 可hash，
    #value任意数据类型，
    #dict 优点：二分查找去查询
                #存储大量关系型数据
        #特点：无序的 3.6  会排序的，没有索引 得通过key查找

# dic = {
#     'name':['大梦','小梦'],
#     'py9':[{'num':71,'avg_age':18},],
#     True:1,
#     (1,2,3):'wuyiyi',
#     2:'erge'
# }
# print(dic)

#增
dic1 = {'name': ['大梦', '小梦'], 'py9': [{'num': 71, 'avg_age': 18}], True: 1, (1, 2, 3): 'wuyiyi', 2: 'erge'}
# dic1['high'] = 185#没有键对应就添加
# dic1['age'] = 16###有键就覆盖

# dic1.setdefault('weight',150)
# print(dic1)#有键对就不覆盖不做任何改变，没有就添加


#删
# dic1.pop('age')   #pop有返回值，按键值删除；没有
# print(dic1.pop('erge',None)) #没有就返回none，可设置返回值
# print(dic1)

# dic1.popitem()  #####默认删除从后面， 返回值是删除的键值元祖

#del dic1['name]#删除，没有则报错
#del dic1
#dic1.clear()##清空字典


#改   update
#dic1['age'] = 16
# dic ={}
# dic2 ={}
# dic2.update(dic)###把dic2中的所有覆盖添加更新

# a = 1
# b = 2
# a,b = b,a
# print(a,b)

#查 for i in value  和keys

# for k,v in dic1.item():
#     print(k,v)##打印元祖和元祖里面的内容

# print(dic1['name1','none'])#打印出对应的值


dic = {
    'name':{'alex','wusir','taibai'},
    'py9':{
        'time':'1213',
        'learn_money':19800,
        'addr':'CBD',
    },
    'age':21
}

#dic ['age'] = 56
#dic ['name'].append('ritian')
#dic ['name'][1] = dic['name'][1].upper()


#female:6

#dic['py9']['female'] = 6

info = input('>>>') #asfjaksfhjaf123ashfjaskd12ksjadhaj12kashd2adj

for i in info:
    if i.isalpha():
        info = info.replace(i,' ')
l = info.split()
print(len(l))