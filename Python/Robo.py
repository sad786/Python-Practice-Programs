x = int(input("Enter the rows = "))
y = int(input("Enter the coloumns = "))

def T(x,y):
	if x==0 or y==0:
		return 1
	else:
		return T(x-1,y)+T(x,y-1)
		
		
print("The total number of ways is ",T(x,y))