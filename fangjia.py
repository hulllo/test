#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys  
import usr.sendemail
import io
import re
try:
    from urllib.parse import urlparse  # py3
except:
    from urlparse import urlparse  # py2

import requests
from bs4 import BeautifulSoup
list = []
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码  
response = requests.get("http://huangqiguandift.fang.com/")
soup = BeautifulSoup(response.content,"html.parser")
tag = soup.find_all('div',class_="fjsstit")[0]
for n in [1,3,5]:                                               #分别获取黄旗观邸，东莞新房，东莞二手房房价
    tag1 = tag.find_all('div',class_="tr01")[n]
    tag2 = tag1.find_all('strong')[0].string
    p = re.sub("\D", "", tag2)
    list.append(p)
    
print(list)
with open('fangjia.txt','a',encoding='utf-8') as fangjia:
    fangjia.write(list[0]+'\t'+list[1]+'\t'+list[2]+'\n')

