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
        # recursive solution DFS
        # TC: O(n), SC: O(n) => recursion stack
        def dfs(root, level):
            if not root: return level
            return max(dfs(root.left, level + 1), dfs(root.right, level + 1))
        
        return dfs(root, 0)

        # recursion solution DFS
        # if not root: return 0
        # return max(self.maxDepthroot(root.left), self.maxDepth(root.right)) + 1

        # iterative solution
        # TC: O(n) => we traverse each node of the tree only once, SC: O(1)
        # queue = deque()
        # level = 0

        # if not root:
        #     return 0
        
        # queue.append(root)
        # while(queue):
        #     for i in range(len(queue)):
        #         node = queue.popleft()

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     level += 1
        
        # return level
