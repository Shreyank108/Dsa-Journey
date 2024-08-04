# class Node : 
#     def __init__(self,item=None,next=None): 
#         self.item=item   
#         self.next=next   

# class SLL: 
#     def __init__(self,start): 
#         self.start=start    
#     def is_empty(self): 
#         return self.start == None 
#     def insert_at_first(self,data): 
#         new_node = Node(data,self.start)
#         self.start= new_node   
#     def insert_at_last(self,data): 
#         new_node= Node(data) 
#         if not self.is_empty: 
#             temp=self.start 
#             while temp.next is not None : 
#                 temp =temp.next    
#             temp.next=new_node     
#         else : 
#             self.start=new_node 
#     def search(self,data): 
#         temp=self.start  
#         while temp.next is not None : 
#             if temp.item == data : 
#                 return temp    
#             temp=temp.next  
#         return None   
    

# mylist=SLL()  
        
# initialize  
# check is it empty or not  
#insert at first   
#insert at last  
#Search 
#Print  

class Node: 
    def __init__(self,item=None, next=None):  
        self.item=item              
        self.next=next    
class SLL: 
    def __init__(self,start=None): 
        self.start=start    
    def id_empty(self): 
        return self.start ==None   
    def inser_at_first(self,data): 
        newNode=Node(data,next=self.start) 
        self.start=newNode   
    def insert_at_last(self,data): 
        newNode=Node(data) 
        if self.start is not None : 
            temp=self.start    
            while temp.next is not None  : 
                temp=temp.next      
            temp.next=newNode   
        else : 
            self.start=newNode   
    def searching(self,data): 
        if self.start is not None : 
            temp=self.start    
            while temp.next is not None : 
                if temp.item ==data :  
                    return temp   
                temp=temp.next  
            return None  
    def insetr_after(self,temp,data): 
        if temp is not None : 
            newNode=Node(data,temp.next) 
            temp.next=newNode    
    def delete_last(self): 
         if self.start is not None : 
            temp = self.start 
            while temp is not None : 
                temp.next=None   
             
    def printing(self): 
        temp=self.start    
        while temp is not None : 
            print(temp.item,end="->") 
            temp=temp.next     


mylist = SLL() 
mylist.inser_at_first(10) 
mylist.inser_at_first(20) 
mylist.insert_at_last(30) 
mylist.insetr_after(mylist.searching(20),50)
mylist.delete_last()
# print(mylist.id_empty())
# print(mylist.searching(20))
mylist.printing()