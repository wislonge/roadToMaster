#process whole database-->file-->dataframe
#pulling and pushing the market
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

rt=0
wr=0
dw=0
up=0		
for i in range(0,StockNum-1): #for every file
	data=pd.read_csv('data/'+namelist[i])
	#lvl,st=pushpull((data['Low'].head(200)))	
	st='pushing'
	actual=data['High'][0]-data['Open'][5]
	if(st=='pushing'):
		if(actual<0):
			rt+=1
			dw+=1
		else:
			wr+=1
			up+=1
	if(st=='pulling'):
		if(actual<0):
			wr+=1
			dw+=1
		else:
			up+=1
			rt+=1
	#print(namelist[i]+':'+'level:'+str(lvl)+'status'+st)

print("wrong num[%d] right num[%d]")%(wr,rt)

print("down num[%d] up num[%d]")%(dw,up)


