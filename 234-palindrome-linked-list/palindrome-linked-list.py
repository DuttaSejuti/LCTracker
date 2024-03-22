# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # TC: O(n), SC: O(n)
        string = ''
        curr = head

        while curr:
            string += str(curr.val)
            curr = curr.next

        if string == string[::-1]:
            return True
        return False