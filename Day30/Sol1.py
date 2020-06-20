# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: ## Solve for the null situation
            return 
        
        self.ans = []
        
        def search(node):
            
            if not node.left and not node.right:
                self.ans.append(node.val)
                return 
            
            if node.left:
                search(node.left)
            
            self.ans.append(node.val)
            
            if node.right:
                search(node.right)
            
        search(root)
        return self.ans
        