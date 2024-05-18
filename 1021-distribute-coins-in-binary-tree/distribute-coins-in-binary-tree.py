# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return (0, 0)

            nodeL, coinL = dfs(root.left) #no of node, no of coin in Left sub-tree
            nodeR, coinR = dfs(root.right)
            self.coinMove += abs(nodeL - coinL) + abs(nodeR - coinR) # abs(node-coin)

            return (nodeL + nodeR + 1, coinL + coinR + root.val)

        self.coinMove = 0
        dfs(root)
        return self.coinMove
