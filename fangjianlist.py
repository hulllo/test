import loupanlist
import requests
from bs4 import BeautifulSoup
loupanlist.loupanlist()
# print(loupanlist.list, loupanlist.addlist) 

response = requests.get("http://dgfc.dg.gov.cn/dgwebsite_v2/Vendition/"+loupanlist.addlist[0])
print("http://dgfc.dg.gov.cn/dgwebsite_v2/Vendition/"+loupanlist.addlist[0])
# soup = BeautifulSoup(response.content,"html.parser")     
# print(soup)
