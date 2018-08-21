import os
import sys
import random
mine="1_2_3_4_5_6_7_"
def daletou(target,source):
	targetr=set()
	targetb=set()
	lines=target.split("_")
        targetr.add(lines[0])
        targetr.add(lines[1])
        targetr.add(lines[2])
        targetr.add(lines[3])
        targetr.add(lines[4])
        targetb.add(lines[5])
        targetb.add(lines[6])
	sourceb=set()
	sourcer=set()
	lines=source.split("_")
        sourcer.add(lines[0])
        sourcer.add(lines[1])
        sourcer.add(lines[2])
        sourcer.add(lines[3])
        sourcer.add(lines[4])
        sourceb.add(lines[5])
        sourceb.add(lines[6])
	bscore=len(sourceb & targetb)
	rscore=len(sourcer & targetr)
	if(rscore==5 and bscore ==2 ):
		return 1
	if(rscore==5 and bscore ==1):
		return 2
	if(rscore==5 and bscore == 0):
		return 3
	if(rscore==4 and bscore ==2):
		return 3
	if(rscore+bscore==5 and bscore!=0):
		return 4
	if(rscore+bscore==4):
		return 5
	if(rscore+bscore==3 or bscore==2):
		return 6


def fulicai(target,source):
	targetr=set()
	targetb=set()
	lines=target.split("_")
        targetr.add(lines[0])
        targetr.add(lines[1])
        targetr.add(lines[2])
        targetr.add(lines[3])
        targetr.add(lines[4])
        targetr.add(lines[5])
        targetb.add(lines[6])
	sourceb=set()
	sourcer=set()
	lines=source.split("_")
        sourcer.add(lines[0])
        sourcer.add(lines[1])
        sourcer.add(lines[2])
        sourcer.add(lines[3])
        sourcer.add(lines[4])
        sourcer.add(lines[5])
        sourceb.add(lines[6])
	bscore=len(sourceb & targetb)
	rscore=len(sourcer & targetr)
	if(rscore==6 and bscore ==1 ):
		return 1
	if(rscore==6 and bscore ==0):
		return 2
	if(rscore==5 and bscore == 1):
		return 3
	if(rscore+bscore == 5 ):
		return 4
	if(rscore+bscore == 4 ):
		return 5
	if(bscore == 1):
		return 6
	# if(rscore+bscore==5 and bscore!=0):
	# 	return 4
	# if(rscore+bscore==4):
	# 	return 5
	# if(rscore+bscore==3 or bscore==2):
	# 	return 6


def gen(r,n):
	b=set()
	while(len(b)<n):
		b.add(int(random.uniform(1,r)))
	return b
def genString():
	b=gen(17,1)
	r=gen(33,6)
	a=""
	for num in r:
		a=a+(str(num)+"_")
	for num in b:
		a=a+str(num)+"_"
	return a
	
targetr=set()
targetb=set()
simTarget=open("data/simTarget.txt")
contents=simTarget.readlines()
s_total=len(contents)
s_scores=[0,0,0,0,0,0]
for line in contents:
	genss=genString()
	ret=fulicai(line,genss)
	if(ret!=None):
		print(line+":::::"+genss)
		print(ret)
		s_scores[ret-1]+=1



print(s_scores)
print(float(s_scores[5])/s_total)
print(float(s_scores[4])/s_total)
print(float(s_scores[3])/s_total)
print(s_total)
simTarget.close()
