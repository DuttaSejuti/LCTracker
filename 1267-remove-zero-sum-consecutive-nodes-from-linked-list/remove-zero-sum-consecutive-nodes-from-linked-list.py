# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def linked_list_to_array(self, head: Optional[ListNode]) -> List:
        new_list = list()
        curr = head

        while curr:
            new_list.append(curr.val)
            curr = curr.next
        return new_list

    def array_to_linked_list(self, array: List) -> Optional[ListNode]:
        if not array:
            return None

        linked_list = ListNode(array[0])
        curr = linked_list

        for i in range(1, len(array)):
            curr.next = ListNode(array[i])
            curr = curr.next
        return linked_list

    def remove_zero_sum_subarray_from_array(self, array: List) -> List:
        prefix_sum = 0
        store_map = dict() # prefix_sum : index
        store_map[0] = -1 # so that if a zero-sum occurs in the array, we would know from where to srart removinf

        result = list()
        
        # [2, 2]
        # i = 2
        # idx = 0
        for i in range(len(array)):
            prefix_sum += array[i]
            if prefix_sum in store_map:
                idx = store_map[prefix_sum]
                result = array[:idx+1] + array[i+1:]
            else:
                store_map[prefix_sum] = i
        return result

    def zero_sum_subarray_exists(self, array: List) -> bool:
        prefix_sum = 0
        store_map = dict() # prefix_sum : index
        store_map[0] = -1 # so that if a zero-sum occurs in the array, we would know from where to srart removinf

        for i in range(len(array)):
            prefix_sum += array[i]
            if prefix_sum in store_map:
                return True
            else:
                store_map[prefix_sum] = i
        return False
        
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        array = self.linked_list_to_array(head)

        while(self.zero_sum_subarray_exists(array)):
            array = self.remove_zero_sum_subarray_from_array(array)

        return self.array_to_linked_list(array)
