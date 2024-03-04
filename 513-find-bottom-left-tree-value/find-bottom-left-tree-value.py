# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findHightestLevel(self, root: Optional[TreeNode]) -> int:
        level = 0
        queue = deque()

        if root:
            queue.append(root)

        while(len(queue) > 0):
            for i in range(len(queue)):
                v = queue.popleft()
                if v.left:
                    queue.append(v.left)
                if v.right:
                    queue.append(v.right)
            level += 1

        return level
        
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        h = self.findHightestLevel(root)
        level = 0

        if root:
            queue.append(root)

        while(len(queue) > 0):
            for i in range(len(queue)):
                v = queue.popleft()
                if level+1 == h:
                    return v.val
                if v.left:
                    queue.append(v.left)
                if v.right:
                    queue.append(v.right)
            level += 1
