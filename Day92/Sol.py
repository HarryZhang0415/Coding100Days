from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  # TODO: Write your code here
  fast, slow = head, head

  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
  
  reverse_head_second = reverse(slow)

  ans = head

  while head is not None and reverse_head_second is not None:
    if head == slow:
      break
    next = head.next
    head.next = reverse_head_second
    reverse_head_second = reverse_head_second.next
    head.next.next = next
    head = head.next.next
  head.next = None
  
  return ans

def reverse(head):
  prev = None
  while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next
  
  return prev

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()
