class Node: 
    def __init__(self,item=None, next =None ) : 
        self.item = item    
        self.next=next    

class SLL : 
    def __init__(self) : 
        self.head = None      
        self.n = 0    
    
    def __len__(self): 
        return self.n  
    
    #inserting  
    
    def insert_at_start(self,data): 
        newNode= Node(data)                      
        newNode.next = self.head    
        self.head = newNode     
        self.n=self.n+1      
        
    def insert_from_tail(self,data): 
        newNode=Node(data)  
        if self.head is None : 
            self.head = newNode   
            self.n = self.n+1    
            return  
        current = self.head    
        while current.next is not None :
            current = current.next    
        current.next = newNode    
        newNode.next =None    
        
    def insert_after(self,after,data): 
        newNode= Node(data) 
        current = self.head    
        while current is not None : 
            if current.item == after: 
                break    
            current = current.next    
        
        if current is not None : 
            newNode.next = current.next   
            current.next = newNode    
            self.n= self.n+1   
        else : 
            return "Item Not Found "  
        
    #inserting  
    
    #Deletion
    def clear(self): 
        self.head =None   
        self.n = 0    
        
    def deletion_from_head(self): 
        if self.head is None : 
            return "No more deletion can take place ,,, its empty" 
        else : 
            self.head = self.head.next  
            self.n=self.n-1  
            
    def deletion_from_tail(self): 
        
        if self.head is None : 
            return "Already Empty"
        
        current = self.head    
        
        if current.next ==None : 
            return self.deletion_from_head()
        
        while current.next.next is not None  : 
            current = current.next    
        current.next= None                
        self.n=self.n-1  
        
    def deletion_from_anywhere(self,data): 
        current = self.head    
        while current.next is not None : 
            if current.next.item == data :  
                break       
            current = current.next    
        if current.next is None : 
            return "Not Found" 
        else :   
            current.next= current.next.next    
        
            
            
        
        
    #Deletion  
    
    #Traversing 
    
    def traverse(self): 
        current = self.head    
        while current is not None : 
            print (current.item,end="->") 
            current=current.next   
        print(None) 
    
        
        

            
            
sll=SLL() 
sll.insert_at_start(4)
sll.insert_at_start(3)
sll.insert_at_start(2)
sll.insert_at_start(1) 
sll.insert_from_tail(5)
sll.insert_after(3,400)
# sll.deletion_from_head()
# sll.deletion_from_tail() 
sll.deletion_from_anywhere(4)
sll.traverse()
         