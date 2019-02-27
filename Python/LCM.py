a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

di = 2
res = 1
while a!=1 or b!=1:
	if a%di==0 and b%di==0:
		a = int(a/di)
		b = int(b/di)
		res*=di
	elif b%di==0:
		b = int(b/di)
		res*=di
	elif a%di==0:
		a = int(a/di)
		res*=di
	else:
		di+=1
		
print("LCM is ",res)
		
