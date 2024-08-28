class Node: 
    def __init__(self,data): 
        self.data=data    
        self.left=None   
        self.right=None   
def insert(root,key): 
    if root is None : 
        return Node(key) 
    elif key < root.data  : 
        root.left=insert(root.left,key) 
    else : 
        root.right=insert(root.right,key)   
    return root

def inorder(root): 
    if root :  
        inorder(root.left)
        print(root.data,end=" ") 
        inorder(root.right) 
def preorder(root): 
    if root :  
        print(root.data,end=" ") 
        preorder(root.left)
        preorder(root.right) 
def postorder(root): 
    if root :  
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")  
    
def searching(root,key): 
    if root is None or root.data == key: 
        return root    
    elif key< root.data : 
        return searching(root.left,key) 
    else : 
        return searching(root.right,key)  
    
def deletion(root,key): 
    if root is None : 
        return root   

    elif key < root.data : 
        root.left=deletion(root.left,key) 
        
    elif key > root.data : 
        root.right= deletion(root.right,key) 
    
    else : 
        
        #  left node   
        if root.left is None and root.right is None : 
            root =None    
            
        #single child   
        elif root.left is None : 
            root = root.right  
        
        elif root.right is None : 
            root= root.left   
        
        #two child  
        
        #method 1 [Sucessor] 
        
        # else : 
        #     temp = minvalue(root.right) 
        #     root.data = temp.data 
        #     root.right = deletion(root.right,temp.data)
         
        #method 2 [predeccesor]  
        else : 
            temp = max_value(root.left)  
            root.data=temp.data   
            root.left=deletion(root.left,temp.data)
    return root   

def minvalue(node): 
    current = node  
    while current.left is not None : 
        current = current.left   
    return current
def max_value(node): 
    current = node  
    while current.right is not None : 
        current = current.right   
    return current
                 

root = None  

l=[4,7,6,3,9,10,34,2,89] 
for key in  l:
    root=insert(root,key)  
    
#printing   
inorder(root)
print()
preorder(root) 
print()
postorder(root) 
print()

# key =7
# result = searching(root,key) 
# if result : 
#     print("Element Founded ") 
# else : 
#     print("No element founded") 
print("THE EXAMINE ") 

inorder(root) 
print()
deletion(root,10) 
inorder(root)



