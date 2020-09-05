# Solution 1: Dynamic programming
'''
Save the ancestor of a node in the list ans, if the node equals p or q, save the list
merge the two list and return the last one of the merged-list
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dic = {}
        def search(node, ans, p, q):           
            if not node:
                return
            if node == p or node == q:
                self.dic[node] = ans + [node]
            search(node.left, ans + [node], p, q)
            search(node.right, ans + [node], p, q)
            
        
        search(root, [], p, q)
        ans_p = self.dic[p]
        ans_q = self.dic[q]
        
        ans = [i for i in ans_p if i in ans_q]
        
        return ans[-1]


### Solution 2 ## much more grace way

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if (left and right) or (root in [p,q]):
            return root
        else:
            return left or right