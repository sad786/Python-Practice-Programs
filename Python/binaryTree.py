class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None



class Tree:
    def __init__(self):
        self.__root = None
        
    def add(self,data):
        if self.__root == None:
            node = Node(data)
            self.__root = node
        else:
            data_node = self.__root
            
            temp_node = data_node
            
            while temp_node:
                if data<temp_node.data:
                    data_node = temp_node
                    temp_node = data_node.left
                else:
                    data_node = temp_node
                    temp_node = data_node.right
                    
            if data_node.data<data:
                data_node.right = Node(data)
            else:
                data_node.left = Node(data)
                    
                
    
    
    def remove(self,data):
        pass
    
    
    def pre_order_traverse(self):
        def traverse(node):
            if node ==None:
                return;
            print(node.data)
            traverse(node.left)
            traverse(node.right)
        traverse(self.__root)
        
    def post_order_traverse(self):
        def traverse(node):
            if node == None:
                return
            traverse(node.left)
            traverse(node.right)
            print(node.data)
        
        traverse(self.__root)
        
    def inorder_traverse(self):
        
        def traverse(node):
            if node==None:
                return
            #print(node.data)
            traverse(node.left)
            print(node.data)
            traverse(node.right)
        
        traverse(self.__root)
        
        
        
        
if __name__ == '__main__':
    print('Enter the number of element you want to add')
    
    binary_tree = Tree()
    for i in range(int(input())):
        binary_tree.add(int(input()))
        
    
    print('Here is the preorder traversal')
    binary_tree.pre_order_traverse()
    
    print('Here is the post order traversal')
    binary_tree.post_order_traverse()
    
    print('Here is the In order traversal')
    binary_tree.inorder_traverse()
    
    