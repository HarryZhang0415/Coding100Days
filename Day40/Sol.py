# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        stack = []
        while True:
            if not head:
                return None
            if head not in stack:
                stack.append(head)
            else:
                return head
            
            head = head.next
        
        