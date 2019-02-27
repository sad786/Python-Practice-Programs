x = eval(input("Enter the list of names: "))
even =0
odd =0
for i in x:
	if len(i)%2==0:
		even+=1
	else:
		odd+=1
		
print("Even names are",even)
print("Odd names are",odd)