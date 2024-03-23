# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMid(self,head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # print("mid", slow)
        return slow
    
    def reverse(self, mid: Optional[ListNode]) -> Optional[ListNode]:
        curr = mid
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # print("prev", prev)
        # print("mid", mid)
        return prev
    
    def merge(self, head: Optional[ListNode], reversedSecondHalf: Optional[ListNode]) ->  Optional[ListNode]:
        list1, list2 = head, reversedSecondHalf

        while list2:
            next_list1 = list1.next
            next_list2 = list2.next

            if next_list1 == list2:
                next_list1 = None

            list1.next = list2
            list2.next = next_list1

            list2 = next_list2
            list1 = next_list1

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # print("head", head)
        mid = self.findMid(head)
        # print("mid", mid)
        reversedSecondHalf = self.reverse(mid)
        # print("reversed",revervedSecondHalf)
        self.merge(head, reversedSecondHalf)
        