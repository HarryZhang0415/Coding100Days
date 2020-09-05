# Accepted

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ans = {}
        
        def search(node, flag):
            if not node:
                return
            if flag in self.ans.keys():
                self.ans[flag].append(node.val)
            else:
                self.ans[flag] = [node.val]
            
            search(node.left, flag + 1)
            search(node.right, flag + 1)
        
        search(root, 0)
        
        self.ans1 = []
        for key in self.ans.keys():
            self.ans1.append(self.ans[key])
        
        return self.ans1
        