# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.values = []
        
        def search(node):
            if not node:
                return
            
            self.values.append(node.val)
            
            search(node.left)
            search(node.right)
        
        search(root)
        
        return sorted(self.values)[k-1]