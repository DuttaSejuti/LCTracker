# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        queue = deque()

        if not root:
            return
        
        queue.append(root)

        while(queue):
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

        # iterative DFS
        # if not root:
        #     return
        
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     node.left, node.right = node.right, node.left
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        # return root

        # pre-order DFS
        # if not root:
        #   return 
        # if root:
        #     root.left, root.right = root.right, root.left
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        # return root
