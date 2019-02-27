
'''
armstrong number is the number if every digit
by adding will be the same as original number is called palindrome number
'''


x = int(input("Enter any number = "))

n = x
res = 0
r =0
while n>0:
	r+=1
	n = int(n/10)
n = x
while n>0:
	t = int(n%10)
	res = res+t**r
	n = int(n/10)
	
if res==x:
	print(x,"is armstrong number")
else:
	print(x,"is not armstrong number")