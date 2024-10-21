# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def dfs(self, root: Optional[TreeNode], target: int, pathSum: int) -> bool:
#         if not root:
#             return False

#         pathSum += root.val
        
#         if not root.left and not root.right and pathSum == target:
#             return True
#         res = False
#         if root.left:
#             res |= self.dfs(root.left, target, pathSum)
#         if root.right:
#             res |= self.dfs(root.right, target, pathSum)

#         pathSum -= root.val
#         return res

#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         pathSum = 0
#         return self.dfs(root, targetSum, pathSum)
        
class Solution:
    def dfs(self, root: Optional[TreeNode], target: int, pathSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right and pathSum + root.val == target:
            return True

        res = False
        if root.left:
            res |= self.dfs(root.left, target, pathSum + root.val)
        if root.right:
            res |= self.dfs(root.right, target, pathSum + root.val)

        return res

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathSum = 0
        return self.dfs(root, targetSum, pathSum)
        