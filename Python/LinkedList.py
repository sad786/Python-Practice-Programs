# this program is to test reverse list in using Linked List data structure

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        #self.tail = None
        
    
    #inserting node at the end of the linked list
    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            
            temp.next = Node(data)
            
    
    
    #check if the list is empty
    def is_empty(self):
        return self.head ==None
        
    #View of the linked list
    #def __repr__(self):
    
    #check if there is any cycle in linedlist
    def is_cycle(self):
        if not self.is_empty():
            temp = self.head
            while temp:
                if temp.next == temp:
                    print(f'There is cycle between at {temp.data}')
                    break
                temp = temp.next
            print('There is no cycle')
        else:
            print('List is empty')
            
    
    def __str__(self):
        if not self.is_empty():
            temp = self.head
            while temp:
                print(temp.data,end=' ')
                temp = temp.next
            print()
        return ''
    
    #to reverse the list
    def reverse(self):
        if not self.is_empty():
            prev = None
            current = self.head
            #temp = current.next
            
            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            #current.next = prev
            self.head = prev
    
    # delete the node
    def delete_node(self,key):
        if not self.is_empty():
            if key == self.head.data:
                self.head = self.head.next
            else:
                temp = self.head
                prev = None
                find = False
                while temp:
                    if temp.data == key:
                        prev.next = temp.next
                        find = True
                        break
                    prev = temp
                    temp = temp.next
                
                if not find:
                    print(f'{key} is not present in the list')
        

if __name__ == '__main__':
   linkedlist = LinkedList()
   linkedlist.insert_at_end(10)
   linkedlist.insert_at_end(12)
   linkedlist.insert_at_end(11)
   linkedlist.insert_at_end(1)
   linkedlist.insert_at_end(91)
   linkedlist.insert_at_end(41)
   linkedlist.insert_at_end(61)
   linkedlist.insert_at_end(5)
   linkedlist.insert_at_end(3)
   linkedlist.insert_at_end(2)
   linkedlist.insert_at_end(1)
   
   print(linkedlist)
   linkedlist.reverse()
   print(linkedlist)
   linkedlist.is_cycle()
   
   linkedlist.delete_node(1)
   linkedlist.delete_node(10)
   print(linkedlist)