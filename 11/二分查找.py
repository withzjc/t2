#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : 二分查找.py
# Author : cjz
# Date  : 2019/1/13 15:01

# 二分查找 必须处理有序的列表
l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]

# def find(l,aim):
#     mid_index = len(l)//2
#     if l[mid_index]<aim:
#         new_l = l[mid_index+1:]
#         find(new_l,aim)
#
#     elif l[mid_index] > aim:
#         l[:mid_index]
#         new_l = l[mid_index + 1:]
#         find(new_l,aim)
#     else:
#         print('找到了',mid_index,l[mid_index])
#
# find(l,66)

def find(l,aim,start =0,end =None):
    end = len(l) if end is None else end
    mid_index = (end -start) //2 +start
    if start <= end:
        if l[mid_index] <aim:
            find(l,aim,start =mid_index+1,end=end)
        elif l[mid_index] > aim:
            find(l,aim,start=start,end=mid_index-1)
        else:
            print('找到了',mid_index,aim)

find(l,44)

# 参数 end
# 返回值
# 找不到的话怎么办