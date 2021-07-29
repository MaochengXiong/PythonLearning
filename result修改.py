import numpy as np
import os 
import csv

def getFiles(path):
    files = [(path + '\\' + f) for f in os.listdir(path)]
    return files

def getResult(path):
    result=["a_min", "a_max", "a_interval", "a_mean", "a_var", "a<0.5","a>2.0", "p_min","p_max","p_interval","p_mean", "p_var","p_amplitude","type","filename"]
    for file in getFiles(path):
        type=False
        if file.startswith("C:\\Users\\Sean\\Desktop\\NandPtest\\dataTest1\\fall"):
            type = True
        temp = np.loadtxt(file,delimiter=',', skiprows=1,usecols=[1,2,3,5], dtype='double',encoding='gbk')
        acc = accelaration(temp[:,0],temp[:,1],temp[:,2])
        
            
        res = count(acc, temp[:,3])
        res.append(type)
        res.append(fileName)
        # print(count(acc, temp[:,3]).append([type,fileName]))
        result = np.vstack((result, res))
        # print(result, res)
    return result

def accelaration(ax,ay,az):
    a=(ax**2+ay**2+az**2)**0.5/255
    return a

def count(a,p):
    count1=0; count2=0 
    a_min=min(a); a_max=max(a); a_mean=np.mean(a); a_var=np.var(a)
    for i in a:
        if(i<0.5): count1=count1+1
        if(i>2.0): count2=count2+1   
    p_min=min(p); p_max=max(p); p_mean=np.mean(p); p_var=np.var(p); p_amplitude=p_max-p_min
    a_interval=abs((np.argwhere(a==a_max)[0][0]-np.argwhere(a==a_min)[0][0])*120)
    p_interval=abs((np.argwhere(p==p_max)[0][0]-np.argwhere(p==p_min)[0][0])*120)       
    return  (["%.3f"%a_min, "%.3f"%a_max, a_interval, "%.3f"%a_mean, "%.5f"%a_var,count1, count2, "%.3f"%p_min,"%.3f"%p_max,p_interval,"%.3f"%p_mean, "%.5f"%p_var,"%.3f"%p_amplitude])

def creatCSV(a):
    with open("result.csv",'w+',newline='') as t:
        writer = csv.writer(t)
        writer.writerows(a)


creatCSV(getResult("C:\\Users\\Sean\\Desktop\\NandPtest\\dataTest1\\fall"))