import os
import sys
import _parse_HLAer

from _parse_HLAer import HLAer
os.system("rm list.txt")
os.system("ls data>list.txt")
fp=open('list.txt')
namelist=fp.read()
namelist=namelist.split('\n')
print(names[2])
for i in range(40,50):
	result=HLAer(namelist[i])
print result

