## 难点在于设置初值为 -inf 和 inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def search(node, left, right):
            if not node:
                return True
            
            if node.val <= left or node.val >= right:
                return False
            
            if not node.left and not node.right:
                return True
            else:
                return search(node.left, left, node.val) and search(node.right, node.val, right)
        
        return search(root, float('-inf'), float('inf'))
        