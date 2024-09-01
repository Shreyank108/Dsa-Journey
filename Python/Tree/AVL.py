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
            return self.rightrotate(root) 
        if balance < -1  and key < root.right.data: 
            root.right= self.rightrotate(root.right) 
            return self.leftrotate(root)
         
        return root  
    
    def leftrotate(self,root): 
        y=root.right 
        T2= y.left  
        y.left = root   
        root.right= T2    
        root.height= 1+max(self.getheight(root.left),self.getheight(root.right))
        y.height= 1+max(self.getheight(y.left),self.getheight(y.right)) 
        return y  
    
    def rightrotate(self,root): 
        y=root.left 
        t2=y.right    
        y.right = root   
        root.left = t2 
        root.height= 1+max(self.getheight(root.left),self.getheight(root.right))
        y.height= 1+max(self.getheight(y.left),self.getheight(y.right))
        return y    
    
    def getheight(self,root): 
        if not root : 
            return 0  
        return root.height   
    
    def getbalance(self,root ): 
        if not root : 
            return 0   
        return self.getheight(root.left)-self.getheight(root.right)  
    def inorder(self,root): 
       self.inorder(root.left) 
       print(root.data,end=" ") 
       self.inorder(root.right) 
       

avl_tree = AVL()
root = None
keys = [10, 20, 30, 40, 50, 25]

for key in keys:
    root = avl_tree.insert(root, key)

avl_tree.inorder(root) 
        
         
            