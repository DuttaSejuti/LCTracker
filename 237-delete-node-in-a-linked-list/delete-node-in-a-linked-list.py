# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# IDEA
# head = [4,5,1,9], node = 1
# node looks like this => ListNode{val: 5, next: ListNode{val: 1, next: ListNode{val: 9, next: None}}}
# here, node is the one we need to remove(5), so, we have to replace the node's value(5) with the next
# node's value(1), and point the next node to the next node of 1 which is 9 in this case.
# Basically we are removing the required node by rewriting it with the next node's properties (val, next)

class Solution:
    def deleteNode(self, node):
        next_node = node.next 
        node.val = next_node.val
        node.next = node.next.next
        node

        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        