# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.ans = 0
        def search(node, tmp_count):
            if not node:
                self.ans = max(self.ans, tmp_count - 1)
                return
            
            search(node.left, tmp_count + 1)
            search(node.right, tmp_count + 1)
        
        search(root, 1)
        return self.ans