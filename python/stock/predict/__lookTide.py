#this script calculate the stock vector and catagory them to different group
import os
import sys
import numpy as np
import pandas as pd

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
	return level
def stock_vector_gen(name):
	data=pd.read_csv('data/'+name)
	#meanv=np.mean(data['High'].head(50))
	lvl=pushpull(data['High'].head(200))
	variation=np.std(data['High'].head(50))
	return (lvl,variation)







