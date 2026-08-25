# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #input is ordered
        # make it not 
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        first = head

        # reverse it
        prev = None
        curr = second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second = prev #[10 is the first]

        while first and second:
            first_next = first.next
            second_next = second.next
            
            first.next = second
            if first_next :
                second.next = first_next
            first = first_next
            second = second_next
        # slow = head
        # fast = head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        
        # second = slow.next # [8,10]
        # slow.next = None #[2,4,6]
        # first = head

        # # reverse it
        # prev = None
        # curr = second

        # while curr :
        #     next_node = curr.next
        #     curr.next = prev

        #     prev = curr #[8,10]
        #     curr = next_node
        # second = prev #[10,8,None]

        # while first and second :
        #     first_next = first.next
        #     second_next = second.next

        #     first.next = second
        #     if first_next:
        #         second.next = first_next

        #     first = first_next
        #     second = second_next


 


        
