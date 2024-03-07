# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# IDEA
# 1) get the length of the linked list, if even m = l // 2, else m = l//2 + 1; then traverse
# the linked list with i = 1 and return head while i == m
# 2) use slow-fast paced two pointer, traverse the linked list with slow, fast pointer, if !fast
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow