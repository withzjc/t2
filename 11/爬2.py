

import requests
import re

#定义第一个函数  目的：获取分类里面的小说

def  get_novel_list():
    '''
    获取小说url，请求导航栏的url
    :return:
    '''
    response = requests.get('http://www.quanshuwang.com/list/1_1.html')
    response.encoding = 'gbk'
    # print(response.text)


get_novel_list()