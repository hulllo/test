# coding=utf-8
from __future__ import unicode_literals
import logging
import os
import re
import time
import io  
import sys  
try:
    from urllib.parse import urlparse  # py3
except:
    from urlparse import urlparse  # py2

import pdfkit
import requests
from bs4 import BeautifulSoup

list = []
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码  
response = requests.get("http://gaoqing.fm/")
soup = BeautifulSoup(response.content,"html.parser")
# for string in soup.find_all(class_='tr01')[3].stripped_strings:
    # print(repr(string))
tag = soup.find_all('div',style="padding:5px;padding-bottom:10px;border-bottom:2px #ccc dotted")
for tag1 in tag[1].find_all('div',style="position:relative;float:left"):
    
    for y in tag1.stripped_strings:
        list.append(y)
        # print(y)
# for x in tag1.stripped_strings:
    # print(x)
    
for tag2 in tag[1].find_all('a',target="_blank",style="font-size:12px"):
    list.append(tag2.string)
    # print(tag2.string)
print (list)   
input()
  