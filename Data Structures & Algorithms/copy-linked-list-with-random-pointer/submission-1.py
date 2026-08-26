"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # deep copy
        # different completely
        # copy only the value
        #copy_nodes = Node(head.val)
        old_to_new = {}
        
        curr = head

        while curr :
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # result the head
        curr= head

        # iterate and mapping
        while curr : 
            old_to_new[curr].next= old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new.get(head)