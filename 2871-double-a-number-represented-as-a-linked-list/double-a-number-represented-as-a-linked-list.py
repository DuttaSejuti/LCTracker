# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        curr = head
        # we need this prev var/node, becasue if after doubling the last_node of the reversed ll we still have a carry = 1
        # we need to add this 1 as a new_node
        prev = None
        carry = 0

        while curr:
            val = curr.val * 2 + carry
            curr.val = val % 10
            
            # carry can not be more than 1, because the node.val will be in range 0 to 9
            if val > 9:
                carry = 1
            else:
                carry = 0
            
            prev = curr
            curr = curr.next
        
        if carry:
            prev.next = ListNode(carry)

        return self.reverse(head)
