# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        self.ans = {}
        
        def search(node, level):
            if not node:
                return
            
            self.ans[level] = node.val
            
            search(node.left, level + 1)
            search(node.right, level + 1)
        
        search(root, 0)
        
        return [v for k,v in sorted(self.ans.items(), key = lambda x:x[0])]