# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# IDEA
# INPUT => head = [1,2,3,4,5], n = 2, OUTPUT => [1,2,3,5]
# we measure the length of the linkedList, then compute the index we need to remove
# then remove the node by pointing the prev node's next to the removed node's(4) next(5)
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
                prev.next = curr.next
                break
            prev = curr 
            curr = curr.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLength(head)

        nodeToBeRemovedIndex = length - n + 1 # 1-index; idx from the start
        
        # if the node to be remove is the head itself, then head becomes None
        if nodeToBeRemovedIndex == 1: 
            return head.next

        self.deleteNode(head, nodeToBeRemovedIndex)
        return head
        