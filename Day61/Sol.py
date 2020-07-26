'''
recursion solution

Algorithm:

1. Start traversing the graph from head node
2. If we already have a cloned copy of the current node in the visited dictionary, we use the cloned node reference.
3. If we don't have a cloned copy in the visited dictionary, we create a new node and add it to the visited dictionary. visited_dictionary[current_node] = cloned_node_for_current_node.
4. We then make two recursive calls, one using the random pointer and the other using next pointer. 
   The diagram from step 1, shows random and next pointers in red and blue color respectively. 
   Essentially we are making recursive calls for the children of the current node. 
   In this implementation, the children are the nodes pointed by the random and the next pointers.
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.hashmap = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: # head is None, so we return None
            return None 

        if head in self.hashmap:
            return self.hashmap[head]

        self.hashmap[head] = Node(head.val, None, None)

        self.hashmap[head].next = self.copyRandomList(head.next)
        self.hashmap[head].random = self.copyRandomList(head.random)

        return self.hashmap[head]