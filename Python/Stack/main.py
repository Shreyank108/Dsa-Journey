class Node : 
    def __init__(self,item=None,next=None) : 
        self.item=item   
        self.next=next    

class Stack : 
    def __init__(self): 
        self.top= None    
    
    def isempty(self): 
        return self.top==None  
    
    def push(self,data): 
        newNode=Node(data) 
        newNode.next=self.top       
        self.top= newNode  
        
    def peek(self): 
        if (self.isempty()): 
            print("Empty")
        else :
            print(self.top.item) 
        
    def pop(self): 
        self.top= self.top.next    
    
    def traverse(self): 
        current = self.top 
        while current is not None : 
            print(current.item,end="->")  
            current=current.next
        print(None )

stack = Stack() 
stack.push(1)         
stack.push(2)         
stack.push(3)  
stack.push(5) 
stack.pop() 
stack.traverse()   
stack.peek()  
            