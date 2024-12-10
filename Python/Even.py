
#
#k = int(input())

#if k%3==0:
#   print('sexy')
#elif (k-2)%3==0:
#    print('pretty')
#elif (k-1)%3==0:
#    print('beautiful')
#else:
#    print('Nothing')
#


'''
#Take input here
#we will take input using ast sys
import ast
input_str = input()

#ast.literal_eval() will evaluate the string and make a data structure for the same
#here the input is a list since input is in '[...]', so ast.literal_eval() will
#make a list with the same data as passed
input_list = ast.literal_eval(input_str)

#the data or the two values in list is now changed to separate variables
day_of_the_week = input_list[0] #first element is an integer denoting the day of the week
is_on_vacation = input_list[1] #this is a boolean denoting if its vacation or not

# write your code here

if is_on_vacation and day_of_the_week in [1,2,3,4,5]:
    print('10:00')
elif is_on_vacation and day_of_the_week in [6,7]:
    print('off')
elif not is_on_vacation and day_of_the_week in [1,2,3,4,5]:
    print('7:00')
elif not is_on_vacation and day_of_the_week in [6,7]:
    print('10:00')
    
'''

'''
def factorial(n):
    if n>=0:
        i = 1
        fact = i
        while i<=n:
            fact = fact *i
            i+=1
        return fact
    else:
        return -1

n = int(input())

print(factorial(n))
'''


'''
def rev(num):
    res = 0
    while (num%10) >0:
        res = res*10 + num%10
        num = num//10
    return res
    

num = int(input())

print(rev(num))
'''
'''
input_list = input().split(',')

m = int(input_list[0])
c = int(input_list[1])


choc = m//c
wrap = choc

while wrap//3 !=0:
    choc = choc + wrap//3
    wrap = wrap//3 + wrap%3
    
print(choc)

'''


n = int(input())

for i in range(n):
    for j in range(i,n//2+1):
        for k in range(i,j//2):
            print('*_',end='')
        print(' ',end='')
    print('*')
        