#volume compare from numpy lib

import os
import sys
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
from predict import predict
os.system("rm list.txt")
os.system("rm data/list")
os.system("ls data>list.txt")
fp=open('list.txt')
namelist=fp.read()
namelist=namelist.split('\n')
print("num of stocks %d")%(len(namelist))
StockNum=len(namelist)

#for i in range(0,StockNum-1): #for every file
print("try to open file"+namelist[1])
data=pd.read_csv('data/'+namelist[1])
plt.subplot(2,1,1)
#plt.plot(data['High'].head(20))
#plt.plot(data['Low'].head(20))
plt.plot(data['High'].head(20)-data['Low'].head(20))
plt.subplot(2,1,2)
plt.plot(data['Volume'].head(20))
plt.show()
