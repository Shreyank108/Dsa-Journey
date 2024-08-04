# class Node: 
#     def __init__(self,item=None,next=None): 
#         self.item=item   
#         self.next=next   
# class SLL: 
#     def __init__(self,start=None): 
#         self.start=start    
        
#     def is_empty(self): 
#         return self.start == None    
    
#     def insert_at_first(self,data): 
#         newNode= Node(data,next=self.start) 
#         self.start =newNode  
        
#     def insert_at_last(self,data): 
#         newNode=Node(data) 
#         if self.start is not None : 
#             temp= self.start    
#             while temp.next is not None : 
#                 temp = temp.next    
#             temp.next=newNode   
#         else : 
#             self.start = newNode   
            
#     def searching(self,data):  
#         if self.start is not None : 
#             temp=self.start    
#             while temp.next is not None  : 
#                 if temp.item == data : 
#                     return temp    
#                 temp=temp.next
#             return None   
        
#     def insert_after(self,temp,data): 
#         if temp is not None : 
#             newNode = Node(data,temp.next) 
#             temp.next=newNode 
    
#     def delete_first(self): 
#         if self.start is not None : 
#             temp=self.start    
#             while temp is not None : 
#                 temp.next=None  
                
#     def delete_last_node(self):
#         if self.start is None : 
#             pass              
#         elif self.start.next is None: 
#             self.start =None   
#         else : 
#             temp=self.start   
#             while temp.next.next is not None : 
#                 temp=temp.next    
#             temp.next=None 
    
#     def to_delete(self,data): 
#         if self.start is None : 
#             pass                         
#         elif self.start.next is None : 
#             if self.start.item ==data :    
#                 self.start =None    
#         else : 
#             temp=self.start   
#             if temp.item ==data :             
#                 self.start =temp.next   
#             else : 
#                 while temp.next is not None : 
#                     if temp.next.item ==data :   
#                         temp.next=temp.next.next    
#                         break    
#                     temp= temp.next   
               
#     def printing(self): 
#         temp=self.start   
#         while temp is not None : 
#             print(temp.item , end="->") 
#             temp=temp.next   
#         print(None)  
       
# mylist= SLL() 
# mylist.insert_at_first(10) 
# mylist.insert_at_first(20)  
# mylist.insert_at_last(30)
# mylist.insert_at_last(40)
# mylist.insert_at_last(50)  

# mylist.to_delete(30)


# mylist.printing()
