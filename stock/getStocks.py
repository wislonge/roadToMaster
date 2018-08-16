
from __future__ import print_function
import pandas as pd
import os
import sys
import threading
url='http://table.finance.yahoo.com/table.csv?s='


def download_data(which,code):
	if which=='shanghai':
		urltarget=url+'%06d'%(code)+'.ss'
		os.system('wget -P data -t 3 -T 10 '+urltarget)
	else:
		urltarget=url+'%06d'%(code)+'.sz'
		os.system('wget -P data -t 2 -T 10 '+urltarget)
#	print(szlist.head(100))

class myThread (threading.Thread):

    def __init__(self, threadID, whichd, codeNum):

        threading.Thread.__init__(self)

        self.whichd = whichd

        self.codeNum = codeNum
    def run(self):
	download_data(self.whichd,self.codeNum)


if not os.path.exists('shanghai.xlsx'):
	print('shang hai stock list is null')
else:
	sslist=pd.read_excel('shanghai.xlsx')

if not os.path.exists('shenzhen.xlsx'):
	print('shenzhen stock list is null')
else:
	szlist=pd.read_excel('shenzhen.xlsx')

sslistsize=sslist.size

for stocks in range(0,sslistsize):
	temp=myThread(stocks,'shanghai',sslist.ix[stocks])
	temp.start();

