# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.que = collections.deque()
               
        def search(node):
            if not node:
                return
            
            search(node.left)
            self.que.append(node.val)
            search(node.right)
        
        search(root)
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            return self.que.popleft()
        else:
            return None
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.que:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()