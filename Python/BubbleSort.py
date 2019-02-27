n = int(input("Enter size of the list"))
list = []
while n>0:
	list.append(int(input("Enter values of List one by one")))
	n-=1

# here i am applying bubble sor to sort the list
for i in range(len(list)-1,0,-1):
	for j in range(i):
		if list[j]>list[j+1]:
			t = list[j]
			list[j] = list[j+1]
			list[j+1] = t
			
print("After sorting the list elements are")
for e in list:
	print(e,end=' ')