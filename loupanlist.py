#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#返回两个参数：楼盘地址、链接

from __future__ import unicode_literals
import sys  
# import usr.sendemail
import io
import re
try:
    from urllib.parse import urlparse  # py3
except:
    from urlparse import urlparse  # py2

import requests
from bs4 import BeautifulSoup
list = []
addlist = []
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8') #改变标准输出的默认编码  
def loupanlist():
    with open("bbs.txt",'w',encoding='utf-8') as bbs:
        # for n in range(10):
        response = requests.get("http://dgfc.dg.gov.cn/dgwebsite_v2/Vendition/ProjectInfo.aspx?New=1")
        soup = BeautifulSoup(response.content,"html.parser")
        tag = soup.find_all('table',id="resultTable")[0]
        for tag1 in tag.find_all('tr',class_="oddTr"):
            tag2 = tag1.find_all("a")[0].string
            # print(tag2)
            list.append(tag2)
            addlist.append(tag1.a['href'])
            # print(tag1.a['href'])

        for tag1 in tag.find_all('tr',class_="evenTr"):
            tag2 = tag1.find_all("a")[0].string
            list.append(tag2)
            addlist.append(tag1.a['href'])
        # print(list, addlist)      
    return(list,addlist)    
