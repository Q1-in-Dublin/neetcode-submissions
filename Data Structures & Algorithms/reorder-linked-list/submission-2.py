# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #input is ordered
        # make it not 

        #first and second

        fast = head
        slow = head

        # arrived to the middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #split into two
        #[2,4,6,8,10]
        second = slow.next #[8,10]
        slow.next = None #first [2,4,6,None]
        first = head

        #reverse it (second)

        prev = None
        curr = second 
#[ none 8 10 ]
        while curr : 
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second = prev
        #put one by one

        while first and second:
            first_next = first.next
            second_next = second.next

            first.next = second
            if first_next : 
                second.next = first_next
            
            first = first_next
            second = second_next




        
