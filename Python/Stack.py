# This is Stack implementation using in built list

class Stack:
    def __init__(self):
        self.stack = []
        
        
    def pop(self):
        if self.size() >0:
            return self.stack.pop()
        return 'Stack Underflow Error'
        
    def push(self, data):
        self.stack.append(data)
        
    def peek(self):
        if self.size() >0 :
            return self.stack[-1]
        return 'Stack Underflow'
        
    def size(self):
        return len(self.stack)
        
    
    def __str__(self):
        if self.size()>0:
            print(self.stack[::-1])
            
        return ''
        
if __name__ == '__main__':
    stack = Stack()
    stack.push(11)
    stack.push(12)
    stack.push(23)
    stack.push(10)
    
    print(stack)
    print(stack.pop())
    print(stack.peek())
    print(stack)