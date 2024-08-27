# class Node: 
#     def __init__(self,data=None)  : 
#         self.data=data   
#         self.left=None 
#         self.right=None  
        
#     #     '''
#     #          1
#     #     2           3
#     # 4       5
#     #     '''
    
# root=Node(1)                  #level1   

# root.left=Node(2)             #Level 3
# root.right=Node(3)  

# root.left.left=Node(4)        #Level 4
# root.left.right=Node(5) 

# #Traversing    BFS,DFS   

# #BFS -> Normal   
# #DFS -> InOrder , PreOrder , PostOrder

# #inorder   left->root->right   
# #preorder  root->left->right 
# #postorder left->right->root 

# def inorder(root): 
#     if root : 
#         inorder(root.left) 
#         print(root.data,end=" ") 
#         inorder(root.right)  
        
# def preorder(root):
#     if root:
#         print(root.data,end=" ") 
#         preorder(root.left) 
#         preorder(root.right) 

# def postorder(root):
#     if root: 
#         postorder(root.left)
#         postorder(root.right)
#         print(root.data,end=" ")

# print("Inorder traversal ",end="")        
# inorder(root)
# print("\n")
# print("preorder traversal ",end="")        
# preorder(root)
# print("\n")
# print("post traversal ",end="")        
# postorder(root)


# BFS => Breadth First Search    

# we use queue  wit enqueueu and deequeue operations 
    
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    