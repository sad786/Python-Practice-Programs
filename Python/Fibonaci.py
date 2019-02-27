
'''
	In fibonaci series next number is sum of previous two numbers 
	e.g = 0,1,1,2,3,5,8,13,21,34,55
	each digit of above series is the sum of its leftmost two predicesors
'''

x = int(input("Enter the range = "))
for i in range(x+1):
	if i==0:
		print(0,end="")
	elif i==1:
		print(1,end="")
	else:
		print((i-1)+(i-2),end="")