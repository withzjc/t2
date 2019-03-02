# s = 'alexwusir'
# s1 = s.capitalize()
# print(s1)
#
# s2 = s.upper()
# s21 = s.lower()
# print(s2,s21)
#
#
# #不区分大小写
# '''s_str = 'acEQ'
# your_input = input('请输入验证码不区分大小写')
# if s_str.upper() == your_input.upper():
#     print('success')
# else:
#     print('请重新输入')'''
#
# #大小写翻转
# s3 = s.swapcase()
# print(s3)
#
# #首字母大写
# s = 'alex egon wusir'
# s4 = s.title()
# print(s4)
#
# #居中 空白填充
# s5 = s.center(20,'#')
# print(s5)
#
#
# s6 = s.expandtabs()
# print(s6)
#
# #公共方法
# l=len(s)
# print(l)
#
# #判断字符串什么开头endswith
# '''s = 'ssssssaffafafasf'
# s7 = s.startswith('as')
# if s7:
#     pass
# elif s.startswith('bl'):
#     pass
# print(s7)'''
#
# s71 = s.startswith('e',2,5)
# print(s71)
#
#
# #判断字符串有没有s，  find,找不到返回-1
# s = 'alexWUsir'
# s8 = s.find('W',2,3)
# print(s8)
#
# #index通过元素找索引，找不到返回-1
#
# s81 = s.index('A')
# print(s81)
#
# #去空格,strip(),输入啥写的单个最小元素就删啥
# s = 'alex  wu  SIR '
# s9 = s.strip()
# print(s9)
# usrname = input('please enter:').strip()
#     if usrname =='cunge'
#         print('congratulation!')
#
# s = 'alexWUsir%'
# s91 = s.strip('%')
# print(s91)
#
#
# #rstrip从右边删，lstrip从左边删
#
# #count数数，统计个数,没有就是0（整体与个数
# s = 'alexa wusir1'
# s10 = s.count('a',2,6)
# print(s10)
#
# #split一分为二，
# s = 'alex :Wusir taibai'
# s11 = s.split(':')
# print(s11)
#
# #format格式化输出
# s = '我叫{}，今年{}，爱好{}。宅说一下我叫{}'.format('taibai',34,'nv','taibai')
# print(s)#######按顺序
#
# s = '我叫{0}，今年{1}，爱好{2}。宅说一下我叫{0}'.format('taibai',34,'nv','taibai')
# print(s)#######索引
# #可迭代对象，多个对象组成的
#
# s = '我叫{name}，今年{age}，爱好{hobbie}。宅说一下我叫{name}'.format(name='taibai',age=34,hobbie='nv',name='taibai')
# print(s)
#
#
#
# #replace默认全部替换，
# s = 'sanajkfhakfhaljkfs'
# s12 = s.replace('ha','辣鸡',4)
# print(s12)
#
# #is 是什么，字符串是不是由。。。组成的
# s = 'sdjasfkalsfjlak'
# for i in s:
#     print(i)#####依次打印，，有限循环
#
# s = 'ajdfiafjai拆解爱adsjaisd'
# if '拆解爱' in s:
#     print('您的评论有敏感词。。。')

