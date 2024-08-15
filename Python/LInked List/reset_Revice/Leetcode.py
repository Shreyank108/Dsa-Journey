class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def __init__(self): 
        self.head = None     
    
    def insert(self, data): 
        newNode = ListNode(data) 
        newNode.next = self.head    
        self.head = newNode  
    
    def deleteNode(self, node):
        if self.head and self.head.val == node:
            self.head = self.head.next
            return
        
        current = self.head
        while current and current.next:
            if current.next.val == node:
                current.next = current.next.next
                return
            current = current.next
        
        print("Node with value", node, "not found.")
        
    def traverse(self): 
        current = self.head    
        while current is not None: 
            print(current.val, end="->") 
            current = current.next  
        print(None) 
    
# Example usage
sol = Solution() 
sol.insert(1)    
sol.insert(12)    
sol.insert(3)     
sol.insert(34)    
sol.insert(346)   

sol.deleteNode(3) 
sol.traverse()
