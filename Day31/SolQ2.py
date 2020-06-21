# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def search(node):
            if not node:
                return None
            
            if not node.left and not node.right:
                return node
            
            left_tail = search(node.left)
            right_tail = search(node.right)
            
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            
            return right_tail if right_tail else left_tail
        
        search(root)
        
            
            