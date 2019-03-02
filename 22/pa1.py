#!/usr/bin/python3
# -*- coding : utf-8 -*-
# File   : pa1.py
# Author : cjz
# Date  : 2019-03-02 11:30
import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
url_temp = "https://www.zhihu.com"

r = requests.get(url_temp,headers= headers)

print(r.status_code)
