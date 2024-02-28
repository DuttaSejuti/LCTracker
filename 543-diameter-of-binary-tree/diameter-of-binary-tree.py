# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global ans
        ans = 0
        def height(root):
            global ans
            if not root:
                return 0
            left = 0
            right = 0
            if root.left:
                left = height(root.left) + 1
            if root.right:
                right = height(root.right) + 1

            ans = max(ans, left+right)
            return max(left, right)

        height(root)
        return ans