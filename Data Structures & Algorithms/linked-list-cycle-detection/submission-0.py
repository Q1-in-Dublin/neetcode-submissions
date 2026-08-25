# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # singly-linked
        # try to find it repeat it

        rabbit=head
        tort=head

        #rabbit is None itself? or can go one more step??
        while rabbit and rabbit.next:
            tort = tort.next
            rabbit = rabbit.next.next

            if tort == rabbit:
                return True

        return False
