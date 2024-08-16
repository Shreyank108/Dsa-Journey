class Node: 
    def __init__(self,item=None, next =None )  : 
        self.item= item    
        self.next =next    
    
class Sll: 
    def __init__(self):   
        self.head =None
        self.n =0 
    
    def __len__(self): 
        return self.n               

    def inser_at_head(self,data): 
        newNode=Node(data) 
        newNode.next=self.head    
        self.head = newNode   
        self.n= self.n+1  
    
    def inset_at_tail(self,data): 
        newNode=Node(data) 
        current = self.head    
        while current.next is not None : 
            current = current.next   
        current.next =newNode 
        newNode.next = None   
        self.n= self.n+1   
        
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
            self.n= self.n+1              
            
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
            
    # Searching 
    def searching(self,value):  
        current = self.head
        pos=0     
        while current is not None : 
            if current.item == value : 
                return pos   
            current = current.next   
            pos+=1  
        return "ni hai element bro" 
    
    def __getitem__(self, index): 
        current = self.head   
        pos =0   
        while current is not None : 
            if pos == index   : 
                return current.item  
            current= current.next   
            pos +=1 
        return      
    # Searching   
    
    def replace_with_max(self,value): 
        current = self.head   
        max = current  
        while current is not None :
            if current.item > max.item  : 
                max = current    
            current= current.next    
        max.item = value 
        
    def summ_of_odd(self): 
        current = self.head  
        counter =0  
        resultant =0   
        while current is not None :  
            if counter %2 != 0 : 
                resultant = resultant + current.item 
            counter+=1  
            current=current.next   
        print(resultant) 
        
    def reversing_linked_list(self): 
        prev= None      
        current = self.head     
        while current is not None :    
            next_node= current.next    
            current.next = prev    
            prev = current    
            current= next_node    
        self.head = prev     
        
    def finding_middle_elem(self):  
        slow= self.head    
        fast = self.head   
        while fast is not None and fast.next is not None : 
            slow=slow.next   
            fast = fast.next.next   
        print(slow.item)
            
        
            
    def traversing(self): 
        current = self.head    
        while current is not None : 
            print (current.item,end="->") 
            current=current.next    
        print(None) 
        
sll=Sll() 
sll.inser_at_head(100)
sll.inset_at_tail(1)
sll.inset_at_tail(2)
sll.inset_at_tail(3)
sll.inset_at_tail(4)
sll.inset_at_tail(5)
sll.inset_at_tail(6)
# sll.insert_after(40,200)
# sll.clear()
# sll.deletion_of_head()
# sll.delete_from_tail() 
# sll.delete_value(400)
# sll.delete_value(30) 
# print(sll.searching(30)) 
# sll.replace_with_max(98) 
# sll.summ_of_odd()
# sll.reversing_linked_list() 
sll.traversing()  
print(len(sll))
sll.finding_middle_elem()
sll.traversing()
        