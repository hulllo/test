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
with open("bbs.txt",'w',encoding='utf-8') as bbs:
    for n in range(10):
        response = requests.get("https://bbs.hassbian.com/forum.php?mod=forumdisplay&fid=38&orderby=dateline&orderby=dateline&filter=author&page="+str(n+1))
        soup = BeautifulSoup(response.content,"html.parser")
        tag = soup.find_all('div',class_="mn")[0]

        for tag1 in soup.find_all('tbody',id=re.compile(r'normalthread_\w*')):
            tag2 = tag1.find_all('a',class_="s xst")[0].string
            print(tag2)
            bbs.write(tag2+'\n')
# for n in [1,3,5]:                                               #分别获取黄旗观邸，东莞新房，东莞二手房房价
    # tag1 = tag.find_all('div',class_="tr01")[n]
    # tag2 = tag1.find_all('strong')[0].string
    # p = re.sub("\D", "", tag2)
    # list.append(p)
    
# print(list)
# with open('fangjia.txt','a',encoding='utf-8') as fangjia:
    # fangjia.write(list[0]+'\t'+list[1]+'\t'+list[2]+'\n')

