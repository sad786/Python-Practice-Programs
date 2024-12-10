

class Des():
    def __init__(self):
        print('The object is created')
       
    def __del__(self):
        print('The Object is destroyed')
        

if __name__=='__main__':
    d = Des()
    del d;print('after destroying object')
    
    
    