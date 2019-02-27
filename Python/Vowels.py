str = input().strip()
n = int(input())

def check(s):
	if s=='a'or s=='e' or s=='i' or s=='o' or s=='u':
		return True
	return False
	

def non_vowels(str,n):
	i,index =0,0
	start = 0
	res = 0
	non_vowels = 0
	
	disturb_flag = True
	while index<len(str):
		if disturb_flag:
			if not check(str[index]):
				non_vowels +=1
		else:
			if not check(str[start]) and check(str[index]):
				non_vowels -=1
			elif not check(str[index]):
				non_vowels +=1
			if non_vowels<n:
				disturb_flag = True
			start +=1
		if disturb_flag and non_vowels>=n:
			if res==0:
				res = index +1
			else:
				res = res+1
			disturb_flag = False
		index +=1
	if disturb_flag:
		return -1
	return res
	
	
res = non_vowels(str,n)		
print(res)