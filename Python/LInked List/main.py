class Node : 
    def __init__(self,item=None, Next=None): 
           self.items=item    
           self.Next=Next    
    
class SLL: 
    def __init__(self,start): 
        self.start=start     
    def is_empty(self): 
        return self.start ==None      
    def insert_at_first(self,data): 
        new_node = Node(data,self.start) 
        self.start =new_node  
    def insert_at_last(self,data): 
        new_node =Node(data) 
        if not self.is_empty():  
            pass
             
            