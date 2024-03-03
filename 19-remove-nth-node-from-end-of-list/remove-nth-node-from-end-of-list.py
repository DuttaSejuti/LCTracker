# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# IDEA
# INPUT => head = [1,2,3,4,5], n = 2, OUTPUT => [1,2,3,5]
# we measure the length of the linkedList, then compute the index we need to remove
# then remove the node; we replace the removed node's(4) property with the next node's(5) property

class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        count = 0
        curr = head
        while(curr):
            count += 1
            curr = curr.next
        return count

    def deleteNode(self, head: Optional[ListNode], idx: int) -> None:
        i = 0
        curr = head
        prev = head
        while(curr):
            i += 1
            if i == idx:
                next_node = curr.next
                if next_node:
                    curr.val = next_node.val
                    curr.next = next_node.next
                else:
                    prev.next = None # if the node to be removed is the tail node
                break
            prev = curr 
            curr = curr.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLength(head)

        # the lowest value of n can be 1, if the length of the linkedList is 1, there is only 1 node
        # if we have to remove that node, the head becomes None
        if length == 1:
            head = None
            return head

        nodeToBeRemovedIndex = length - n + 1 # 1-index
        self.deleteNode(head, nodeToBeRemovedIndex)
        return head
        