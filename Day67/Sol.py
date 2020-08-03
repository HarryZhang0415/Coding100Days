# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_l1 = []
        stack_l2 = []
        
        while l1:
            stack_l1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack_l2.append(l2.val)
            l2 = l2.next
        
        ans = []
        
        remain = 0
        flag = 0
        
        while stack_l1 and stack_l2:
            number = stack_l1.pop(-1) + stack_l2.pop(-1) + flag
            remain = (number)  % 10 
            flag = (number)  // 10 
            
            ans.append(remain)
        
        if stack_l1:
            while stack_l1:
                number = stack_l1.pop(-1) + flag
                remain = (number)  % 10 
                flag = (number)  // 10 

                ans.append(remain)
        
        if stack_l2:
            while stack_l2:
                number = stack_l2.pop(-1) + flag
                remain = (number)  % 10 
                flag = (number)  // 10 

                ans.append(remain)
            
        if flag != 0:
            ans.append(flag)
            
        ans3 = ans2 = ListNode(0)
        while ans:
            ans2.next = ListNode(ans.pop(-1))
            ans2 = ans2.next
        
        return ans3.next