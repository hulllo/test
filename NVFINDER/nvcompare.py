import re
import os
class Qcn_old():
    nvid = []
    description = []
    value = []
class Qcn_new():
    nvid = []
    description = []
    value = []
nvdata = []  
oldqcn = Qcn_old()
newqcn = Qcn_new()   
nvid = []  
nvolddata = []
nvnewdata = []
nv_counter = 0
nv_found_counter = 0
nv_not_found_counter = 0
with open('qcn_old.xml') as qcnolddata:    #打开查找目标QCN xml文件
    for x in qcnolddata:                 #将QCN xml文件的各条目加入列表nv
        x = x.replace('\n','') 
        nvolddata.append(x)  
with open('qcn_new.xml') as qcnnewdata:    #打开查找目标QCN xml文件
    for x in qcnnewdata:                 #将QCN xml文件的各条目加入列表nv
        x = x.replace('\n','') 
        nvnewdata.append(x)         
        
        
with open('nvid.txt') as nvref:  #打开参考NV号文件
    for x in nvref:                 #将参考NV号加入列表nvid
        x = x.replace('\n','') 
        nvid.append(x)       
        
for x in nvolddata:
    oldqcn.nvid.append(''.join(re.findall(r"id=\"(.+?)\" subscriptionid",x)))    #QCN中提取出NVID
    oldqcn.description.append(''.join(re.findall(r"name=\"(.+?)\" mapping",x)))  #QCN中提取出description
    oldqcn.value.append(''.join(re.findall(r">(.+?)<",x)))                       #QCN中提取出value
    
for x in nvnewdata:
    newqcn.nvid.append(''.join(re.findall(r"id=\"(.+?)\" subscriptionid",x)))    #QCN中提取出NVID
    newqcn.description.append(''.join(re.findall(r"name=\"(.+?)\" mapping",x)))  #QCN中提取出description
    newqcn.value.append(''.join(re.findall(r">(.+?)<",x)))                       #QCN中提取出value    
    
with open('result_compare.txt', 'w') as nvresult:   #打开输出文件
    nvresult.write('nvid\tdescription\tresult\told nv value\tnew nv value\n')    
    for x in nvid:   #参考NV号
        if x == '':
            nvresult.write("\n")
            print('\n')
            continue
            
        n = 0
        for y in oldqcn.nvid:
            if x == y:
                oldnvget = oldqcn.value[n]
                break
            else:
                oldnvget = 'not found'     
            n = n+1
            
        n = 0    
        for z in newqcn.nvid:
            if x == z:
                newnvget = newqcn.value[n]
                break
            else:
                newnvget = 'not found'    
            n = n+1
       
        if newnvget == newnvget == 'not found':
            print(x,'Y-not found')
            nvresult.write(str(x)+'\t\tY\tnot found\tnot found\n')
        elif oldnvget == newnvget:
            print(newqcn.nvid[n],'Y')
            nvresult.write(str(newqcn.nvid[n])+'\t'+newqcn.description[n]+'\tY\t'+str(oldnvget)+'\t'+str(newnvget)+'\n')
        else:
            print(newqcn.nvid[n],'N\n',oldnvget,'\n',newnvget)
            nvresult.write(str(newqcn.nvid[n])+'\t'+newqcn.description[n]+'\tN\t'+str(oldnvget)+'\t'+str(newnvget)+'\n')
os.system('notepad result_compare.txt')


