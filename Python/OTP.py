from random import *
t1 = range(0,10)
for j in range(20):
	st=""
	for i in range(6):
		r4 = int(random()*10)
		st = st+str(t1[r4])	
	print("Your OPT is "+st)
	

