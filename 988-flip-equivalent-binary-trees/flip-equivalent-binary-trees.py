# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquiv(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return node1.val == node2.val

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()

        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        
        q1.append(root1)
        q2.append(root2)

        while q1 and q2:
            curr1 = q1.popleft()
            curr2 = q2.popleft()

            if curr1.val != curr2.val: # if the parent node's val doesn't match, False
                return False

            left1, right1 = curr1.left, curr1.right
            left2, right2 = curr2.left, curr2.right

            if self.checkEquiv(left1, left2) and self.checkEquiv(right1, right2):
                if left1: q1.append(left1)
                if right1: q1.append(right1)
                if left2: q2.append(left2)
                if right2: q2.append(right2)
            elif self.checkEquiv(left1, right2) and self.checkEquiv(right1, left2):
                left1, right1 = right1, left1 # flip operation
                if left1: q1.append(left1)
                if right1: q1.append(right1)
                if left2: q2.append(left2)
                if right2: q2.append(right2)
            else:
                return False

        return len(q1) == len(q2) # if the trees are equal, the queues need to be empty
