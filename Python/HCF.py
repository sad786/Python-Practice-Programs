a = int(input("Enter First Number : "))
b = int(input("Enter Second Number: "))
m = min(a,b)
hcf = 1
i = m
while i>=1: 
	if a%i==0 and b%i==0:
		hcf = i
		break
	i-=1
	
print("HCF of {} and {} is {}".format(a,b,hcf))