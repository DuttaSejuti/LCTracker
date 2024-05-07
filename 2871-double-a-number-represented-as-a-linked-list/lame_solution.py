# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_number_from_ll_as_list(self, head: Optional[ListNode]) -> List:
        new_list = []
        curr = head

        while curr:
            new_list.append(curr.val)
            curr = curr.next
        
        return new_list
    
    def convert_list_to_number(self, nums: List) -> int:
        num = 0

        for digit in nums:
            num = num*10 + digit
        
        return num
    
    def double_the_number(self, num: str) -> int:

        return num*2
    
    def convert_num_to_list(self, num: int) -> List:
        if num == 0:
            return [0]

        new_list = []

        while num > 0:
            digit = num%10
            new_list.insert(0, digit)
            num = num//10
        
        return new_list
    
    def convert_list_to_ll(self, num: list) -> Optional[ListNode]:
        res_head = ListNode()
        res_tail = res_head

        for n in num:
            res_tail.next = ListNode(n)
            res_tail = res_tail.next
        
        return res_head.next

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = self.get_number_from_ll_as_list(head)
        num = self.convert_list_to_number(num)
        res_num = self.double_the_number(num)
        res_list = self.convert_num_to_list(res_num)
        res = self.convert_list_to_ll(res_list)

        return res
