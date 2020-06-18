'''
建议先在head前面加一个ListNode，方便处理"[1],1"此类需要对head这个node进行删除操作的情况
'''
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def search(prev, curr, n):
            if not curr:
                return 0
            flag = 1 + search(curr, curr.next, n)
            if flag == n:
                prev.next = curr.next
            
            return flag
        
        
        ans = ListNode(0,head)    
        search(ans, ans.next, n)
        
        return ans.next