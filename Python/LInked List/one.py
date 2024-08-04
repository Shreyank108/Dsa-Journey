#linkde list   

#Singly List 
# class Node : 
#     def __init__(self,data): 
#         self.data=data                      
#         self.next=None   

# #creating
# node1=Node(10) 
# node2=Node(20) 
# node3=Node(30) 
# node4=Node(40) 

# #linking  
# node1.next=node2   
# node2.next=node3  
# node3.next=node4   

# #printing part   
# current = node1   
# while current is not None : 
#     print (current.data,end="->")  
#     current=current.next    
# print(None)


#Doubly Link list   
# class Node : 
#     def __init__(self,data): 
#         self.data=data                      
#         self.next=None   
#         self.prev=None

# #creating
# node1=Node(10) 
# node2=Node(20) 
# node3=Node(30) 
# node4=Node(40) 

# #linking  next 
# node1.next=node2   
# node2.next=node3  
# node3.next=node4   

# #linking prev 
# node4.prev=node3 
# node3.prev=node2
# node2.prev=node1

# #printing part  forward 
# current = node1   
# while current is not None : 
#     print (current.data,end="->")  
#     current=current.next    
# print(None) 

# #printing part Backward   
# current =node4  
# while current is not None  : 
#     print(current.data,end="->") 
#     current=current.prev   
# print(None)

#circular Linked list   
# class Node : 
#     def __init__(self,data): 
#         self.data=data                      
#         self.next=None   
#         self.prev=None

# #creating
# node1=Node(10) 
# node2=Node(20) 
# node3=Node(30) 
# node4=Node(40) 

# #linking  next 
# # node1.next=node2   
# # node2.next=node3  
# # node3.next=node4   
# # node4.next=node1

# # #linking prev 
# node4.prev=node3 
# node3.prev=node2
# node2.prev=node1
# node1.prev=node4

# #printing part  forward 
# # current = node1   
# # start=node1
# # while True : 
# #     print (current.data,end="->")  
# #     current=current.next   
# #     if current == start : 
# #         break  


# #printing part Backward   
# current =node4  
# while True  : 
#     print(current.data,end="->") 
#     current=current.prev   




# class Node: 
#     def __init__(self,data): 
#         self.data=data    
#         self.next=None
    
# #creating    
# node1=Node(10) 
# node2=Node(20) 
# node3=Node(30) 
# node4=Node(40) 

# #linking   
# node1.next=node2   
# node2.next=node3
# node3.next=node4  
# node4.next=node1 

# #printing   
# current = node1   
# while current != None : 
#     print(current.data,end="->")  
#     current=current.next 
# if current ==None : 
#     print(None) 


# dummyhead = ListNode(0) 
# current =dummyhead  
# carry =0    

# while l1 or l2 or carry!=0  : 
#     digit1 = l1.val if l1 is not None else 0    
#     digit2 = l2.val if l2 is not None else 0   
    
#     sum = digit1+digit2 +carry     
#     digit = sum%10    
#     carry=sum//10   
    
#     newNode= ListNode(digit) 
#     current.next=newNode   
#     current=current.next    
    
#     l1= l1.next if l1 is not None else None    
#     l2=l2.next if l2 is not None else None   
    
# result = dummyhead.next    
# dummyhead.next=None   
# return result    

