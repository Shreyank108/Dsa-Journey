class Node : 
    def __init__(self,data=None): 
        self.data=data                 
        self.left=None   
        self.right=None    
def insert(root,key): 
    if root is None : 
        return Node(key) 
    elif key < root.data :  
        root.left= insert(root.left,key) 
    else : 
        root.right = insert(root.right, key) 
    return root     
def inorder(root): 
    if root : 
        inorder (root.left) 
        print(root.data, end=" ") 
        inorder (root.right)   
def postorder(root): 
    if root: 
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
def preorder(root): 
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right) 

def searching (root,key): 
    if root is None or root.data ==key: 
        return root  
    elif root.data > key : 
         return searching(root.left, key) 
    else : 
        return searching(root.right, key)   

def Deletion(root,key): 
    if root is None : 
        return root    
    elif  key < root.data : 
        root.left= Deletion(root.left,key) 
    elif key > root.data : 
        root.right=Deletion(root.right,key) 
    else : 
        if root.left is None and root.right is None : 
            root = None   
        elif root.left is None : 
            root = root.right    
        elif root.right is None : 
            root= root.left    
        else : 
            #Sucessor   [Min Value] 
            temp =min_value(root.right) 
            root.data= temp.data    
            root.right=Deletion(root.right, key) 
    return root  

def min_value(node): 
    current = node   
    while current.left is not None : 
        current = current.left   
    return current  
    


root =None
l=[30,20,10,40,50] 
for i in l: 
    root=insert(root,i) 
    
inorder(root) 
print()
preorder(root) 
print() 
postorder(root) 
print()
# searching(root,50) 


print()
print()
print() 
inorder(root) 
print() 
Deletion(root, 40) 
inorder(root)