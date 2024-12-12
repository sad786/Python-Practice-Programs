# this is stack implementation using linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    
    def push(self,key):
        new_node = Node(key)
        new_node.next = self.top   #this will point new node to the current node
        self.top = new_node    # this will update the top to the new node
    
    def pop(self):
        if self.is_empty():
            return 'Stack Underflow'
        data = self.top.data
        self.top = self.top.next  #move top to the next node
        return data
  
    
    def peek(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.top.data
    
    def __str__(self):
        temp = self.top
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        
        return ''
        
    def is_empty(self):
        return self.top is None
        
        
        
       

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)
    print(stack.peek())
    stack.pop()
    
    print(stack.peek())
    print(stack)