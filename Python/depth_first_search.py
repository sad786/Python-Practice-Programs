class Graph:
    
    def __init__(self):
        self.graph = {'A': ['B','C'],
                      'B': ['A','D'],
                      'C': ['A','E'],
                      'D': ['B','E'],
                      'E': ['C','D']
        }
        
    def find_path(self,source,dest):
        stack = [source]
        path = []
        while stack:
            vert = stack.pop()
            path.append(vert)
            if vert == dest:
                break
            edges = self.graph[vert]
            for v in edges:
                if v not in stack and v not in path:
                    stack.append(v)
            
        
        if path[-1] == dest:
            return path
        else:
            return 'There is no path exist between them'



if __name__=='__main__':
    print('Hello World')
    g = Graph()
    
    res = g.find_path('B','A')
    print(res)