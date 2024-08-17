class Node: 
    def __init__(self,item=None,next=None) : 
        self.item=item   
        self.next=next    

class Queue: 
    def __init__(self): 
        self.front = None    
    
    def enqueue(self,data): 
        newNode= Node(data) 
        newNode.next = self.front   
        self.front = newNode  
        
    def dequeue(self): 
        rear = self.front  
        while rear.next.next is not None :     
            rear = rear.next    
        rear.next=None
        
        
    def traversing(self): 
        rear = self.front  
        while rear is not None : 
            print(rear.item,end="->") 
            rear= rear.next   
        print(None) 

queue=Queue() 
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4) 
queue.enqueue(5) 
queue.traversing()
queue.dequeue()
queue.dequeue()
queue.traversing()