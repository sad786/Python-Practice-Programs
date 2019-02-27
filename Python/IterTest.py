''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import itertools
def main():
    list1 = input().strip().split(" ")
    list2 = input().strip().split(" ")
    A  = set()
    B  = set()
    for e in list1:
        A.add(int(e))
    for e in list2:
		B.add(int(e))
main()

