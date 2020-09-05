# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.ans = float('inf')
        
        def search(node, target):
            if not node:
                return
            
            if abs(target - node.val) < abs(self.ans - target):
                self.ans = node.val
            
            search(node.left, target)
            search(node.right, target)
        
        search(root, target)
        return self.ans


class Solution2:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.ans = float('inf')
        
        def search(node, target):
            if not node:
                return
            
            if abs(target - node.val) < abs(self.ans - target):
                self.ans = node.val
            
            if node.val > target:
                search(node.left, target)
            if node.val < target:
                search(node.right, target)
        
        search(root, target)
        return self.ans