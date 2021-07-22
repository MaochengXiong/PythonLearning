import numpy as np
import os
import csv

# import files in "fall"
path="C:\\Users\\Sean\\Desktop\\NandPtest\\dataTest1\\fall"
fallFiles=os.listdir(path)
# import files in "other"
otherPath="C:\\Users\\Sean\\Desktop\\NandPtest\\dataTest1\\other"
otherFiles=os.listdir(otherPath)
# combine all files in one variable
allFile=fallFiles+otherFiles
# print(allFile)


# declare and initiate the result
res=["a_min", "a_max", "a_interval", "a_mean", "a_var", "a<0.5","a>2.0", "p_min","p_max","p_interval","p_mean", "p_var","p_amplitude","type","filename"]

# get all file in allFile variable for processing 
for file in allFile:
    files = [(path + '\\' + f) for f in os.listdir(path)]
    print(files)
    if file in fallFiles:
        temp=np.loadtxt((path+"\\"+file),delimiter=',', skiprows=1,usecols=[0,1,2,3,5], dtype='double',encoding='gbk')
    elif file in otherFiles:
        temp=np.loadtxt((otherPath+"\\"+file),delimiter=',', skiprows=1,usecols=[0,1,2,3,5], dtype='double',encoding='gbk')
    # count each data in "fall" files for the result (line30-63
    count1=0; count2=0     
    a=(temp[:,1]**2+temp[:,2]**2+temp[:,3]**2)**0.5/255 # count accelaration
    a_min=min(a); a_max=max(a); a_mean=np.mean(a); a_var=np.var(a)   
    # count how many accelation data are less than 0.5 and more than 2.0 separately
    for i in a:
        if(i<0.5): count1=count1+1
        if(i>2.0): count2=count2+1
   
    p=temp[:,4] # get pressure
    p_min=min(p); p_max=max(p); p_mean=np.mean(p); p_var=np.var(p)
    p_amplitude=p_max-p_min
    
# count time      
    a_interval=abs((np.argwhere(a==a_max)[0][0]-np.argwhere(a==a_min)[0][0])*120)
    p_interval=abs((np.argwhere(p==p_max)[0][0]-np.argwhere(p==p_min)[0][0])*120)

    if file in fallFiles: type="True"
    elif file in otherFiles: type="False"    

# merge the data of "fall" count above into result
    res=np.vstack((res,["%.3f"%a_min, "%.3f"%a_max, a_interval, "%.3f"%a_mean, "%.5f"%a_var,count1, count2, "%.3f"%p_min,"%.3f"%p_max,p_interval,"%.3f"%p_mean, "%.5f"%p_var,"%.3f"%p_amplitude,type,file])) 

# create a csv file and save variable res in this file 
with open("result.csv",'w+',newline='') as t:
    writer = csv.writer(t)
    writer.writerows(res)

files = [(path + '/' + f) for f in os.listdir(path)]