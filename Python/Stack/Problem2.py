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
        
        
    def pop(self): 
        data= self.top.item
        self.top= self.top.next 
        return data  
        
    def peek(self): 
        if (self.isempty()): 
            print("Empty")
        else :
            print(self.top.item)   
    
    # def reversing_string(self,data): 
    #     pubic=""
    #     for i in data: 
    #         self.push(i) 
    #     pubic+=self.pop()
    #     print(pubic)
    
    def traverse(self): 
        current = self.top 
        while current is not None : 
            print(current.item,end="->")  
            current=current.next
        print(None )
        
def reversing_string(data): 
        s=Stack() 
        for i in data : 
            s.push(i) 
        pubic="" 
        while (not s.isempty()): 
            pubic= pubic + s.pop() 
        print(pubic) 
        
def type_writing(text,operations): 
    s=Stack() 
    

stack = Stack() 
# stack.push(1)         
# stack.push(2)         
# stack.push(3)  
# stack.push(5) 
# stack.pop() 
reversing_string("Hello")
# stack.traverse()   
# stack.peek()  
            