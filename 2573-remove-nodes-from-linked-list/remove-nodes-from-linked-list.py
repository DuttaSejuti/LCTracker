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
    # without extra memory => TC:O(n) SC:O(1)
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
        head = self.reverse(head)
        curr = head
        currMax = curr.val

        # because the last node of the given ll is the curr, which will always be present
        while curr.next:
            if curr.next.val < currMax:
                curr.next = curr.next.next # remove curr.next
            else:
                currMax = curr.next.val
                curr = curr.next

        return self.reverse(head)

    # solution with stack => TC:O(n), SC:O(n)
    # def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     stack = list()
    #     curr = head

    #     while curr:
    #         while stack and stack[-1] < curr.val:
    #             stack.pop()
    #         stack.append(curr.val)
    #         curr = curr.next
        
    #     result_head = ListNode()
    #     result_tail = result_head

    #     for n in stack:
    #         result_tail.next = ListNode(n)
    #         result_tail = result_tail.next
        
    #     return result_head.next


# class Solution:
    # solution without stack but extra memory => TC: O(n), SC:O(n)
    # def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev = None
    #     curr = head

    #     while curr:
    #         next_node = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next_node
        
    #     return prev

    # def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     curr = self.reverse(head)
    #     currMax = curr.val
    #     result_head = ListNode()
    #     result_tail = result_head

    #     if head is None:
    #         return 
        
    #     while curr:
    #         # get the value that are greater than the previous one's
    #         if currMax <= curr.val:
    #             result_tail.next = ListNode(curr.val)
    #             result_tail = result_tail.next
    #             currMax = curr.val
    #         curr = curr.next
        
    #     if result_head.next is None:
    #         return head
        
    #     return self.reverse(result_head.next)
