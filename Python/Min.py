
def second_min(input_list):
    if(len(input_list)<=1):
        return input_list[0]
    
    Min1 = input_list[0]
    Min2 = input_list[1]
    
    for i in range(2,len(input_list)):
        if Min1>input_list[i]:
            Min1 = input_list[i]
        elif Min2>input_list[i]:
            Min2 = input_list[i]
        
    return Min2 if Min2>Min1 else Min1
    
items = [int(x) for x in input().split(' ')]

print(second_min(items))