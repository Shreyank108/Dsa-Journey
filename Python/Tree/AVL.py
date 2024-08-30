class Node : 
    def __init__(self, data=None): 
        self.data= data    
        self.left =None   
        self.right =None   
        self.height =1    
class AVL : 
    def insert(self,root, key): 
        if root is None : 
            root = Node(key) 
        elif key < root.data : 
            root.left= self.insert(root.left,key) 
        else : 
            root.right= self.insert(root.right,key) 
        
        root.height=1+max(self.getheight(root.left),self.getheight(root.right)) 
        balance= self.getbalance(root) 
        
        if balance >1 and key <root.left.data : 
            return self.rightrotate(root) 
        if balance < -1 and key > root.right.data : 
            return self.leftrotate(root)  
        if balance >1 and key > root.left.data: 
            root.left= self.leftrotate(root.left) 
            return self.righrotate(root) 
        if balance < -1  and key < root.right.data: 
            root.right= self.rightrotate(root.right) 
            return self.leftrotatio(root)
         
        return root  
    
    
        
         
            