#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : 递归函数.py
# Author : cjz
# Date  : 2019/1/13 12:40

# 递归函数:在函数中调用自身函数,最大递归深度997 998，
# 如果递归次数太多就不适合用递归来解决
# 递归的缺点占内存，优点会让代码变简单


import time
def cal_time(func): #装饰器
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("running time:",func.__name__, t2 - t1)
        return result
    return wrapper

@cal_time
def BinarySearch2(target, SortedList, left, right):
    if left > right:
        return -1
    mid = int((left + right) / 2)

    if target == SortedList[mid]:
        return mid
    elif target < SortedList[mid]:
        return BinarySearch2(target, SortedList, left, mid-1)
    elif target > SortedList[mid]:
        return BinarySearch2(target, SortedList, mid+1, right)
    else:
        return -1

SortedList = [17, 20, 26, 31, 44, 54, 55, 77, 93]
# SortedList = [1,2]

res = BinarySearch2(26, SortedList, 0, len(SortedList)-1)
print(res)
