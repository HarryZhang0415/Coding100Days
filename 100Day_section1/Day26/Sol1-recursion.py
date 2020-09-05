'''
Brute Force Solution

The simplest solution is to traverse each node (preorder traversal) and then find all paths which sum to the target using this node as root.
The worst case complexity for this method is N^2.
If we have a balanced tree, we have the recurrence: T(N) = N + 2T(N/2). This is the merge sort recurrence and suggests NlgN.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_path(self, node, target):
        if node:
            return int(node.val == target) + self.find_path(node.left, target - node.val) + self.find_path(node.right, target - node.val)
        else:
            return 0
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root:
            return self.find_path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0
        