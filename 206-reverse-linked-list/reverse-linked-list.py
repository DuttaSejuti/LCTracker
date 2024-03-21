# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# IDEA
# simply picture this 1 -> 2 -> 3 -> 4 -> 5 -> None will become
#  None <- 1 <- 2 <- 3 <- 4 <- 5
#  prev  curr next
#        prev curr next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # TC: O(n), SC:O(1)
    #     prev = None
    #     curr = head
        
    #     while curr:
    #         next_node = curr.next # store the next pointer
    #         curr.next = prev # curr.next will be pointing to the previous node
    #         prev = curr # curr will be the new prev
    #         curr = next_node # we need to traverse the list

    #     return prev

        # Recursion solution
        # TC: O(n), SC: O(n)
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
            def reverse(curr, prev):
                if not curr:
                    return prev

                next_node = curr.next
                curr.next = prev
                
                return reverse(next_node, curr) #basically it's doing curr = next_node, prev = curr

            return reverse(head, None) # initial call curr = head, prev = None
