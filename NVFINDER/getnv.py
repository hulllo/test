import re
import os
class Qcn():
        nvid = []
        description = []
        value = []
nvdata = []  
t = Qcn()   
nvid = []  
nv_counter = 0
nv_found_counter = 0
nv_not_found_counter = 0
input('''
工具说明：获取QCN XML文件里的所有NV号
使用方法：
1.将QCN XML文件更名为qcn.xml，并放在工具同一目录
2.按Enter获取NV号到result_getnv.txt文件''')
with open('qcn.xml') as qcndata:    #打开查找目标QCN xml文件
    for x in qcndata:                 #将QCN xml文件的各条目加入列表nv
        x = x.replace('\n','') 
        nvdata.append(x)  
        
for x in nvdata:
    t.nvid.append(''.join(re.findall(r"id=\"(.+?)\" subscriptionid",x)))    #QCN中提取出NVID
    t.description.append(''.join(re.findall(r"name=\"(.+?)\" mapping",x)))  #QCN中提取出description
    t.value.append(''.join(re.findall(r">(.+?)<",x)))                       #QCN中提取出value
n = 0
with open('result_getnv.txt','w') as getnvid:
    for x in t.nvid:
        getnvid.write(str(t.nvid[n])+'\t'+str(t.description[n])+'\t'+str(t.value[n])+'\n')
        n = n+1
os.system('notepad result_getnv.txt')    
# input('Press Enter to exit...')     