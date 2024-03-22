# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # get the middle point of the LL, slow will point to the middle-last LL (second half)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of the ll (middle-end)
        curr = slow
        second_half = None #prev
        next_node = None

        while curr:
            next_node = curr.next
            curr.next = second_half
            second_half = curr
            curr = next_node
        
        # comparing the first_half to the second_half
        curr = head
        while second_half:
            if curr.val != second_half.val:
                return False
            curr = curr.next
            second_half = second_half.next
        
        return True
        
    # # create a string by traversing the LL and appending the values to the string
    # # check if the reversed string is same or not
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     # TC: O(n), SC: O(n)
    #     string = ''
    #     curr = head

    #     while curr:
    #         string += str(curr.val)
    #         curr = curr.next

    #     if string == string[::-1]:
    #         return True
    #     return False