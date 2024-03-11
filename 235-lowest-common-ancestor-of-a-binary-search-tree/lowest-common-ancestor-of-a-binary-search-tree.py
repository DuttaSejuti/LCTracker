# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# IDEA
# if root is null, return
# 1) If p and q both in left subtree, traverse left subtree
# 2) If p and q both in right subtree, traverse right subtree
# 3) If p and q in different subtree, return current_node/root
# 4) If the current_root/node is p or q, return current_node/root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        
        # Case 1
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Case 2
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Case 3
        if (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
            return root

        # Case 4
        if root.val == p.val or root.val == q.val:
            return root