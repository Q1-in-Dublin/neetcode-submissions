# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #내가 첨에 생각했을때 한노드씩 더해서 만들라고했는데
        #지금 규칙을보니까 맨끝으로가서 여기서서 숫자를 만드는거지
        # 1->2->3 인데 321
        # 4->5->6 인데 이게 654
        # 결국 더하는건 321 + 654니까
        #일단 더하고 뒤집기 같은데
        # Carry

        dummy = ListNode()
        curr = dummy
        carry = 0

        # [7] [5]

        while l1 or l2 or carry :
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            # Calculate carry
            # 12
            total = l1_val+l2_val + carry
            carry = total // 10 #몫 1 
            node_val = total % 10 # Remainer 2
            
            curr.next = ListNode(node_val)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


