# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # singly-linked
        # try to find it repeat it
        # 1 run fast 1 run slow
        # it the loop is there they will meet someday

        fast = head
        slow = head
        #fast is not none and not Non in next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow :
                return True

        return False