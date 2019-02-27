def nextPrime(num):
	while True:
		num+=1
		for i in range(2,num):
			if num%i==0:
				break
		else:
			return num
			
			
def primeProducer(n):
	prime = []
	num,count=1,1
	while count<=n:
		num = nextPrime(num)
		prime.append(num)
		count+=1
	return prime
		
N = int(input("How many prime numbers you want to generate?: "))

l = [x for x in primeProducer(N)]
print(l)