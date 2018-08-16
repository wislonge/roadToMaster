#process whole database-->file-->dataframe
#pulling and pushing the market
import os
import sys
import numpy as np 
import pandas as pd
import  matplotlib.pyplot as plt 
os.system("rm list.txt")
os.system("rm data/list")
os.system("ls data>list.txt")
fp=open('list.txt')
namelist=fp.read()
namelist=namelist.split('\n')
print("num of stocks %d")%(len(namelist))

StockNum=len(namelist)


def pullpower(data):
	sum_pull=0
	data=data-data[0]
	for i in range(0,len(data)):	
		if(data[i]>0):
			sum_pull+=data[i]
	return sum_pull


def pushpower(data):
        sum_push=0
        data=data-data[0]
        for i in range(0,len(data)):
                if(data[i]<0):
                        sum_push+=data[i]
        return abs(sum_push)


def pushpull(data):
	pull=pullpower(data)
	push=pushpower(data)
	if(pull==0 or push==0):
                level=0
        else:
                level=(pull-push)/(pull+push)

	if((pull-push)<0):
		stat='pushing'
	else:
		stat='pulling'
	return (level,stat)
rt=0
wr=0
dw=0
up=0		
for i in range(0,StockNum-1): #for every file
	data=pd.read_csv('data/'+namelist[i])
	lvl,st=pushpull((data['Low'].head(200)))
	
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


