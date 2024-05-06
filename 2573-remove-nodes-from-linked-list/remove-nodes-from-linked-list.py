# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. Reverse the given linked_list, as the last node of the given list will always be present in the result list
# because, there will be no right node for the last node of the given list.
# 2. make the first node value of the reversed list as the currMax.
# 3. create a new LL for the result
# 4. insert the node in the result_ll if it's value is greater than the currMax, upgrade the currMax

class Solution:
    # TC: O(n), SC:O(n)
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
            # get the value that are greater than the previous one's
            if currMax <= curr.val:
                result_tail.next = ListNode(curr.val)
                result_tail = result_tail.next
                currMax = curr.val
            curr = curr.next
        
        if result_head.next is None:
            return head
        
        return self.reverse(result_head.next)
