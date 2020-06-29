# https://leetcode.com/problems/house-robber-iii/discuss/79394/Python-O(n)-code%3A-Optimized-for-Readability

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def search(node):
            if not node:
                return (0,0)
            
            left = search(node.left)
            
            right = search(node.right)
            
            now = node.val + left[1] + right[1]
            
            later = max(left) + max(right)
            
            return (now, later)
        
        return max(search(root))