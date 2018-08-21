import os,sys
import random

simTarget=open("data/simTarget.txt","wr")

a=set()
def gen(r,n):
	b=set()
	while(len(b)<n):
		b.add(int(random.uniform(1,r)))
	return b
for j in range(1000000):
	for num in gen(33,6):
		simTarget.write(str(num)+"_")
	for num in gen(16,1):
		simTarget.write(str(num)+"_")
	simTarget.write("\n")
simTarget.close()
