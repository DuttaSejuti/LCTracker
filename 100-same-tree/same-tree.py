# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# IDEA
# consider when the trees will not be the same
# 1) p.val != q.val => return False
# 2) p.left and !q.left => return False
# 3) p.right and !q.right => return False
# 4) !p.left and q.left => return False
# 5) !p.right and q.right => return False
# consider p.val == q.vall => traverse(p.left, q.left) and (p.right, q.right)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
        