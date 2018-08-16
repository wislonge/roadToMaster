#histogram from numpy lib

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
predict.test(1)
StockNum=len(namelist)

#for i in range(0,StockNum-1): #for every file
data=pd.read_csv('data/'+namelist[200])
a,b=np.histogram(data['High'].head(200),10)
#print(np.histogram(data['High'].head(200),10))
#print(a)
#print(b)
#np.append(a,[0])
plt.hist(data['High'].head(100),20)
plt.title(namelist[200])
plt.text(data['High'][0],10,'current')
plt.show()
