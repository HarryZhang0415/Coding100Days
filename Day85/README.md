# Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


Answer:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            dic = {}

            lp1 = head
            idx = 0

            while lp1:
                dic[idx] = lp1
                lp1 = lp1.next
                idx += 1

            length = max(dic.keys())

            ans = lp2 = ListNode(0, head)

            for i in range(length // 2 + 1):
                lp2.next = dic[i]
                lp2 = lp2.next
                lp2.next = dic[length - i]
                lp2 = lp2.next

            lp2.next = None

            head = ans.next
        else:
            pass
            
        