class Node: 
    def __init__(self,item=None, next =None )  : 
        self.item= item    
        self.next =next    
    
class Sll: 
    def __init__(self):   
        self.head =None
                   
    def inser_at_head(self,data): 
        newNode=Node(data) 
        newNode.next=self.head    
        self.head = newNode    
    
    def inset_at_tail(self,data): 
        newNode=Node(data) 
        current = self.head    
        while current.next is not None : 
            current = current.next   
        current.next =newNode 
        newNode.next = None    
        
    def insert_after(self,after,data): 
        newNode=Node(data) 
        current = self.head    
        while current is not None : 
            if current.item == after  : 
                break    
            current = current.next    
        if current is not None : 
            newNode.next=current.next   
            current.next= newNode 
            
            
    def clear(self): 
        self.head= None   
        
    def deletion_of_head(self): 
        self.head= self.head.next    
        
    def delete_from_tail(self): 
        current = self.head    
        while current.next.next is not None : 
            current = current.next    
        current.next =None  
        
    def delete_value(self,value): 
        current = self.head    
        while current.next is not None : 
            if current.next.item ==  value : 
                break    
            current= current.next   
        if current.next is None : 
            return "ab kya window delete krega" 
        else : 
            current.next= current.next.next       
        
            
    def traversing(self): 
        current = self.head    
        while current is not None : 
            print (current.item,end="->") 
            current=current.next    
        print(None) 
        
sll=Sll() 
sll.inser_at_head(10) 
sll.inser_at_head(20) 
sll.inser_at_head(30) 
sll.inser_at_head(40) 
sll.inset_at_tail(400)
sll.inset_at_tail(800)
sll.insert_after(40,200)
# sll.clear()
# sll.deletion_of_head()
# sll.delete_from_tail() 
sll.delete_value(400)
sll.delete_value(30)
sll.traversing() 
        