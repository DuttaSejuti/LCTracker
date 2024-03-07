# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# IDEA
# 1) get the length of the linked list, if even m = l // 2, else m = l//2 + 1; then traverse
# the linked list with i = 1 and return head while i == m
# 2) use slow-fast paced two pointer, traverse the linked list with slow, fast pointer, if !fast
# or !fast.next, return slow. Simply, return slow when you get to the end of the linked list.

class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        curr = head
        l = 0

        while curr:
            l += 1
            curr = curr.next
        return l
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = self.getLength(head)
        m = (l // 2) + 1
        i = 1
        curr = head

        while curr:
            if i == m:
                return curr
            curr = curr.next
            i += 1

        # TC: O(n), SC: O(1)
        # slow, fast = head, head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # return slow