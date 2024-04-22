# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        left_sum = 0

        if not root:
            return 0
        
        queue.append(root)

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    left_node = curr.left
                    if not left_node.left and not left_node.right:
                        left_sum += left_node.val
                    queue.append(left_node)
                if curr.right:
                    queue.append(curr.right)

        return left_sum
