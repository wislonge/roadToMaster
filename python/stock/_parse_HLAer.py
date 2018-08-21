import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys
# all stock datafile names is in list.txt

def plt_by_name(name):
	#name='table.csv?s=600351.ss'
	data=pd.read_csv('data/'+name)
	#print(data['Date','Open'].head(100))
	print(data.describe())
	print(data.head(100))
	sortdata=data.sort('Date')
	sortdata[['High','Low']].tail(100).plot()
	
	#stock data analysis here
	
	return stockRecommentLevel
#	plt.title(name)
#	plt.show()
