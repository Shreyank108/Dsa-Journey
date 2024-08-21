 
# class Node : 
#     def __init__(self,item = None,next=None): 
#         self.item=item    
#         self.next=next   
         
# class SLL: 
#     def __init__(self,start=None): 
#         self.start=start    
        
#     def isEmpty(self): 
#         return  self.start is None   
    
#     def insert_at_first(self,data): 
#         newNode = Node(data,self.start)  
#         self.start= newNode   
        
#     def insert_at_last(self,data): 
#         newNode= Node(data) 
#         if not self.isEmpty(): 
#             temp=self.start     
#             while temp.next is not None : 
#                 temp=temp.next   
#             temp.next=newNode    
#         else : 
#             self.start = newNode   
            
#     def searching (self,data): 
#         temp=self.start    
#         while temp is not None : 
#             if temp.item ==data  :   
#                 return temp    
#             temp = temp.next     
#         return None    
    
#     def insert_after (self,temp,data): 
#         if temp is not None : 
#             newNode = Node(data,temp.next) 
#             temp.next= newNode    
    
#     def print(self): 
#         temp=self.start    
#         while temp is not None : 
#             print(temp.item , end="->")  
#             temp=temp.next
#         return None   
    
#     def delete_first(self): 
#         if self.start is not None : 
#             self.start =self.start.next    
    
#     def delete_from_last(self): 
#         temp =self.start    
#         while temp.next.next is not None : 
#             temp= temp.next   
#         temp.next=None   
         
#     def delete_particulatr_item(self,data): 
#         if self.start is None   : 
#             pass                     
#         elif self.start.next is None :  
#             if self.start.item == data :  
#                 self.start =None   
#         else : 
#             temp =self.start     
#             if temp.item==data:  
#                 self.start= temp.next    
#             else : 
#                 while temp is not None : 
#                     if temp.next.item == data :   
#                         temp.next=temp.next.next   
#                         break    
#                     temp= temp.next     
#     def __iter__(self): 
#         return SLLIterable(self.start)

# class SLLIterable: 
#     def __init__(self,start): 
#         self.current = start    
#     def __iter__(self): 
#         return self    
#     def __next__(self): 
#         if not self.current : 
#             raise StopIteration 
#         data = self.current.item   
#         self.current = self.current.next   
#         return data                  
    
                    

          
        

# #driver Code   
# mylist = SLL() 
# mylist.insert_at_first(3)
# mylist.insert_at_first(2)
# mylist.insert_at_first(1) 
# mylist.insert_at_last(4) 
# mylist.insert_at_last(5) 
# mylist.insert_at_last(6) 
# mylist.insert_at_last(7) 
# mylist.insert_after(mylist.searching(3),34)
# mylist.delete_particulatr_item(5)
# mylist.print() 

# for i in mylist: 
#     print(" __",i ,"__  ")
        
        
class Node:  
    def __init__(self,value=None,next=None): 
        self.value=value    
        self.next=next    
    
class SLL: 
    def __init__(self): 
        self.head=None    
        self.n=0   
    
    #finding Length    
    def __len__(self): 
        return self.n    
    
    def insert_at_head(self,data): 
        newNode=Node(data) 
        newNode.next=self.head    
        self.head= newNode 
        self.n=self.n+1    
    
    def printing(self): 
        current = self.head
        while current is not None : 
            print(current.value,end="->") 
            current=current.next   
        
    def append(self,data): 
        current = self.head    
        newNode= Node(data)
        while current.next is not None :  
            current= current.next  
        newNode.next =None    
        current.next=newNode  
        self.n=self.n +1  
    
    def insetr_afer(self,after,data): 
        current = self.head 
        newNode=Node(data)   
        while current is not None    :
            if current.value == after : 
               break    
            current = current.next    
        if current is not None : 
            newNode.next = current.next  
            current.next= newNode  
                                
        else : 
            return "Item Not Found "  
    
    def clear(self): 
        self.head=None 
        self.n=0 
        
    def delate_head(self): 
        if self .head == None : 
            return "Empty List" 
        else :
            self.head=self.head.next   
            self.n=self.n-1 
            
    def deleate_from_tail(self): 
        current = self.head    
        if current.next == None : 
           return  self.delate_head() 
        else :
            while current.next.next is not None : 
                current=current.next  
                current.next=None 
        self.n=self.n-1 
        
    def removeing_element(self,data): 
        
        if self.head==None : 
            return "Empty List"
        
        if self.head.value == data: 
             return self.delate_head() 
        
        current=self.head    
        while current.next is not None : 
            if current.next.value == data :              
                break   
            current=current.next   
            
        if current.next == None :  
            return "Nopt Found" 
        else : 
            current.next == current.next.next   
    
    #searching   
    def search_by_index(self,data): 
        current = self.head    
        while current is not None : 
            if current.value == data :  
                print(len(sll)-1)   
            current=current.next 
        return -1    
    
    def Find_middle_elem_and_make_delete(self): 
        slow=self.head  
        prev =None  
        fast=self.head    
        while fast is not None and fast.next is not None : 
            fast=fast.next.next
            prev=slow
            slow=slow.next
        #deleting of Middle Node 
        prev.next = slow.next 
        slow.next=None    
    
        
        
          

    
    
             

sll=SLL()  

sll.insert_at_head(1)
sll.append(2)
sll.append(3) 
sll.append(4) 
sll.append(5) 
sll.append(6) 
sll.append(7) 
sll.printing() 
print("\n")
sll.Find_middle_elem_and_make_delete()
sll.printing() 

