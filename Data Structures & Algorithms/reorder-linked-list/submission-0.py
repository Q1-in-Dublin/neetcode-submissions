# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #input is ordered
        # make it not 

        slow, fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        first = head

        # reverse the second head
        prev = None
        curr = second
        while curr :
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second = prev

        while first and second :
            first_next = first.next
            second_next = second.next

            first.next = second
            if first_next:
                second.next = first_next
            first = first_next
            second = second_next

        
