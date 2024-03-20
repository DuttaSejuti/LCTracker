# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        first = list1
        i = 0

        # finding the (a-1)th node
        while i < a-1:
            first = first.next
            i += 1
        
        # finding the (b+1)th node
        second = first
        while i <= b:
            second = second.next
            i += 1

        # connecting (a-1)th node's next to the list2's head
        first.next = list2

        # traversing list2 to find the tail of list2
        while list2.next:
            list2 = list2.next
        
        # connect list2's next to the (b+1)th node of list1
        list2.next = second
        
        return list1
        