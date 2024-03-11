# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# IDEA
# simply BFS/level order traversing
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # TC: O(n) => we traverse each node of the tree only once
        queue = deque()
        level = 0

        if not root:
            return 0
        
        queue.append(root)
        while(queue):
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        
        return level
