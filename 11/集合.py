'''
集合：可变数据类型。存的元素必须是不可变数据类型，无序，不重复
'''

# set1 = set({1,2,3})
# set2 = {1,2,3}
# print(set1)

#增
set1 = {'alex','wusir','ritian','egon','barry'}
# #add
# set1.add('fake')
# #update  像extend
# set1.update('abc')
# print(set1)

#删除 pop随机删除
# set1.pop()##随机删除，有返回值

#按元素删
# set1.remove('alex')#没有这个元素会报错
# del set1
# #清空 clear（）
#
#
# #查
# for i in set1:
#     print(i)

#求交集
#print(set1 & set2)
#print(set1.intersection(set2))

#求并集
#print(set1 | set2)
#print(set2.union(set1)

#反交集

#差集
#print(set1 - set2)
#print(set1.difference(set2))

#print(set1 < set2)
#print(set1.issubset(set2))#这两个相同说明是set1是2的子集


# li = [1,2,33,44,33,2,4,5,66,66]#去除重复元素
# li = list(set(li))
# print(li)

#freeeze
# s = frozenset('barry')
# print(s.type(s))     变成不可变数据类型
#for i in s:
#    print(i)