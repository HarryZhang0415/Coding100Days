## Sol 1: Brute Force solution --> TLE

'''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = collections.defaultdict(list)
        self.p = p
        self.q = q
                
        def search(prev, curr):
            if not curr:
                return
            if self.p in self.ans.keys() and self.q in self.ans.keys():
                return
            
            self.ans[curr] = self.ans[prev] + [prev] + [curr]
            search(curr, curr.left)
            search(curr, curr.right)
        
        search(root, root)
        
        aces_p = self.ans[p]
        aces_q = self.ans[q]
        
        idx = 0
        
        for aces in aces_p:
            if aces in aces_q:
                idx = max(idx, aces_q.index(aces))
        
        return aces_q[idx]'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dir = {}
        self.p = p
        self.q = q
        self.ans = None
        
        def search(node):
            if not node:
                return False
            
            left = search(node.left)
            right = search(node.right)
            mid = node == p or node == q
            
            if left + right + mid == 2:
                self.ans = node
            
            return left or right or mid
        search(root)
        
        return self.ans
                
                