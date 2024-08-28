if not nums:
            return None
        
        # Find the middle index
        mid = len(nums) // 2
        
        # Create the current root node with the middle element
        root = TreeNode(nums[mid])
        
        # Recursively construct the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root