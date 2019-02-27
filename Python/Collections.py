import collections

def main():
	str = input("Enter any string: ").strip()
	list = []
	list.extend(str)
	count = collections.Counter(list).most_common(2)
	for l in count:
		print(type(l),l,end=" ")
	
main()