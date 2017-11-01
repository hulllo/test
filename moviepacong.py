#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys  
import usr.sendemail
import io
try:
    from urllib.parse import urlparse  # py3
except:
    from urlparse import urlparse  # py2

import requests
from bs4 import BeautifulSoup
directors = []
movie = []
pingfeng = []
links = []
str = ''
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码  
response = requests.get("http://gaoqing.fm/")
soup = BeautifulSoup(response.content,"html.parser")

tag = soup.find_all('div',class_="col-md-9")[0]

for tag1 in tag.find_all('a',target="_blank")[4:100:2]:
	# print(tag1['href'])
	links.append(tag1['href'])
	movie.append(tag1.string)
	# print(tag1.string)
for tag2 in soup.find_all('span',style="color:#CF0000"):
	pingfeng.append(tag2.string)
# n = len(links)	
# print(n)
print(movie)
print(pingfeng)
print(links)
for n in range(len(links)):
	response = requests.get(links[n])
	# print(response)
	soup = BeautifulSoup(response.content,"html.parser")
	# print(soup)
	tag =  soup.find_all('div',class_="col-md-9")[0]
	temp = tag.find_all('a')[5].string
	print(temp)
	directors.append(temp)
print(directors)

n =len(movie)

for x in range(len(movie)):

	str+= movie[x]+'\t'+pingfeng[x]+'\t'+directors[x]+'\n'	

	
with open('movie_data.txt','r') as movie_data:
	data = movie_data.read()

	if data == str:
		print('movie no updata') 
	else:
		with open('movie_data.txt','w') as movie_data:
			movie_data.write(str)	
			usr.sendemail.send_('电影更新','以下是最近更新的电影目录：\n'+str)
		print('send email ok')	

  