# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_length = 0
        def search(node):
            if not node:
                return 0

            left = search(node.left)
            right = search(node.right)

            self.max_length = max(self.max_length, left + right)

            return max(left,right) + 1
        search(root)
        return self.max_length - 1