# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # will keep a hashSet to keep track of the visited node, if the node is already in the set
        # there is a cycle; using hashSet instead of hashMap because there can be duplicate node val
        hash_set = set()
        curr = head

        while(curr):
            if curr not in hash_set:
                hash_set.add(curr)
            else:
                return True
            curr = curr.next

        return False
