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
with open('qcn.xml') as qcndata:    #打开查找目标QCN xml文件
    for x in qcndata:                 #将QCN xml文件的各条目加入列表nv
        x = x.replace('\n','') 
        nvdata.append(x)  
with open('nvid.txt') as nvref:  #打开参考NV号文件
    for x in nvref:                 #将参考NV号加入列表nvid
        x = x.replace('\n','') 
        nvid.append(x)       
        
for x in nvdata:
    t.nvid.append(''.join(re.findall(r"id=\"(.+?)\" subscriptionid",x)))    #QCN中提取出NVID
    t.description.append(''.join(re.findall(r"name=\"(.+?)\" mapping",x)))  #QCN中提取出description
    t.value.append(''.join(re.findall(r">(.+?)<",x)))                       #QCN中提取出value
with open('result_search.txt', 'w') as nvresult:   #打开输出文件
    for x in nvid:
        n = 0
        nv_found = 0
        if x == '':
            nvresult.write("\n")
            continue
        nv_counter = nv_counter + 1
        for y in t.nvid:
            if x == y:
                nv_found = 1
                nv_found_counter = nv_found_counter + 1
                nvresult.write(y+"\t"+t.description[n]+"\t"+t.value[n]+"\n")
                print(y+"\t"+t.description[n]+"\t"+t.value[n])
                break
            n = n+1
        if nv_found == 0:
            nv_not_found_counter = nv_not_found_counter + 1
            nvresult.write(x+"\t\tnv not found\n")
            print(x+"\t\tnv not found")
    nvresult.write("\n\tnv counter:\t"+str(nv_counter)+"\n\tfound:\t"+str(nv_found_counter)+"\n\tnot found\t"+str(nv_not_found_counter))
os.system('notepad result_search.txt')   


