class Node :  
    def __init__(self, data=None): 
        self.data=data                    
        self.left=None  
        self.right=None  

def insertion(root,key): 
    if root is None : 
        return Node (key) 
    elif key < root.data:    
        root.left=insertion(root.left,key) 
    else : 
        root.right = insertion(root.right,key)  
    return root  

def inorder(root): 

    if root : 
        inorder(root.left) 
        l.append(root.data)
        inorder(root.right)


def find_mod(l): 
    m=[]
    p={}
    for i in l: 
        if i in p: 
            p[i]+=1  
        else : 
            p[i]=1   
    print(p)
    for key,value in p.items(): 
        if max(p.values())  == value : 
             m.append(key) 
    print(m)

l=[]

 
root=None   
root=insertion(root,1)       
root = insertion(root,2)
root = insertion(root,3)  
root=insertion(root,4)       
root = insertion(root,3)
root = insertion(root,6)  

inorder(root)
find_mod(l) 


