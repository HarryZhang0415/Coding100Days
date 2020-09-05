# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = collections.defaultdict(list)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def search(node, X, Y):
            if not node:
                return
            
            self.ans[X].append((Y, node.val)) 
            search(node.left, X-1, Y-1)
            search(node.right, X+1, Y-1)
        
        search(root, X=0, Y=0)
        
        tmp_ans = []
        
        for k in sorted(self.ans.keys()):
            tmp_ans.append([x[1] for x in sorted(self.ans[k], key = lambda x:(-x[0],x[1]))])
        
        return tmp_ans
        
    