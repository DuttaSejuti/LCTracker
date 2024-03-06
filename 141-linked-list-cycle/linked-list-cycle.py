# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # keeping a slow and fast pointer, slow increases by 1 node, fast pointer increases by 2 node
        # If the two pointers meets, then there's a cycle
        # TC: O(n), SC:O(1)
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False


        # will keep a hashSet to keep track of the visited node, if the node is already in the set
        # there is a cycle; using hashSet instead of hashMap because there can be duplicate node val
        # in the list.
        # TC:O(n); SC:O(n)

        # hash_set = set()
        # curr = head

        # while(curr):
        #     if curr not in hash_set:
        #         hash_set.add(curr)
        #     else:
        #         return True
        #     curr = curr.next

        # return False
