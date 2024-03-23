# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def reverse(self, mid: Optional[ListNode]) -> Optional[ListNode]:
        curr = mid
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
    
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) ->  Optional[ListNode]:
        while list2:
            next_list1 = list1.next

            list1.next = list2

            list1 = list2
            list2 = next_list1

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
            
        slow, fast, prev = head, head, None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None # 1st half of the LL first - mid; modifying the head to first - mid
        
        mid = slow # LL from middle - end
        reversedSecondHalf = self.reverse(mid)
        self.merge(head, reversedSecondHalf)
        
# class Solution:
#     def findMid(self,head: Optional[ListNode]) -> Optional[ListNode]:
#         slow, fast = head, head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
        
#         # print("mid", slow)
#         return slow
    
#     def reverse(self, mid: Optional[ListNode]) -> Optional[ListNode]:
#         curr = mid
#         prev = None

#         while curr:
#             next_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_node
        
#         # print("prev", prev)
#         # print("mid", mid)
#         return prev
    
#     def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) ->  Optional[ListNode]:
#         while list2:
#             next_list1 = list1.next
#             next_list2 = list2.next

#             if next_list1 == list2:
#                 next_list1 = None
#             # the upper code can be avoided if we keep the prev from the mid
#             # which is breaking the head into first half

#             list1.next = list2
#             list2.next = next_list1

#             list2 = next_list2
#             list1 = next_list1

#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         mid = self.findMid(head)
#         reversedSecondHalf = self.reverse(mid)
#         self.merge(head, reversedSecondHalf)
        