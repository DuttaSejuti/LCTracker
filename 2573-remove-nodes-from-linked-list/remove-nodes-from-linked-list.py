# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = self.reverse(head)
        currMax = curr.val
        result_head = ListNode()
        result_tail = result_head

        if head is None:
            return 
        
        while curr:
            if currMax <= curr.val:
                result_tail.next = ListNode(curr.val)
                result_tail = result_tail.next
                currMax = curr.val
            curr = curr.next
        
        if result_head.next is None:
            return head
        
        return self.reverse(result_head.next)
