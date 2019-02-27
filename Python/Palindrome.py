'''
	palindrome number is the number if we reverse the sequence of the digits then we will get the same number
	
'''
	
x = int(input("Enter any number = "))
n = x
res = 0
while n>0:
	t = int(n%10)
	n = int(n/10)
	res = res*10+t

	
if res==x:
	print(x,"is palindrome number")
else:
	print(x,"is not palindrome number")