#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : 破解zip.py
# Author : cjz
# Date  : 2019/1/7 20:12
import random
import sys
import time
import zipfile
from threading import Thread

'''
    创建一个生成密码的类
'''
class MyIterator():
    '''
    生成密码--》1.密码的生成规则
                2.最小值最大值
    '''
    #创建一个单位字符
    letter = '012345'
    #设置一个最大值和最小值
    min_dig =0
    max_dig =0
    #类的膜法方法---》类自带的
    def __init__(self,min_dig,max_dig):
        '''
        实例化对象是给出密码的范围
        :param min_dig: 最小值
        :param max_dig: 最大值
        '''
        #判断最小值是否小于最大值
        if min_dig < max_dig:
            self.min_dig = min_dig
            self.max_dig = max_dig
        else:
            self.min_dig = max_dig
            self.max_dig = min_dig
    def __iter__(self):
        #返回本身
        return self
    def __next__(self):
        '''
        生成密码，随机匹配的密码，按照上面定义的规则来进行匹配
        :return: 匹配的密码
        '''

        rst = str()#空字符
        for item in range(0,random.randrange(self.min_dig,self.max_dig)):
            rst += random.choice(MyIterator)#匹配的字符规则
        return rst

#定义一个解压压缩包的函数
def extract():
    '''
    提取压缩文件
    :return:
    '''
    start_time = time.time()
   #指定需要解压的文件
    zfile = zipfile.ZipFile('1.zip')
    for p in MyIterator(5,6):
        print(p)
        # 异常的捕获
        # 当出现异常的时候，代码会进行执行
        try:
            #path --->指定解压后文件的存储位置
            zfile.extractall(path='.',pwd=str(p).encode('utf-8'))
            print('这是密码：{}'.format(p))
            #结束时间
            now_time =time.time()

            print('用时：{}'.format(now_time - start_time))
            #执行文件的退出
            sys.exit()

        except Exception as e:
            pass

if __name__ =='__main__':

    t1 = Thread(target=extract)
    t1.start()