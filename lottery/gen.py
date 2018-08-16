import os,sys
import random

simTarget=open("data/simTarget.txt","wr")

a=set()
def gen(r,n):
	b=set()
	while(len(b)<n):
		b.add(int(random.uniform(1,r)))
	return b
def gen12_2():
	return gen(13,2)
def gen35_5():
	return gen(36,5)
for j in range(1000000):
	for num in gen35_5():
		simTarget.write(str(num)+"_")
	for num in gen12_2():
		simTarget.write(str(num)+"_")
	simTarget.write("\n")
simTarget.close()
