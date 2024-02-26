# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # TC: O(P+Q); P:No of nodes in p, Q:No of nodes in q
        if not p and not q: #both are null, then consider same tree and return T
            return True
        if not p or not q: #any one is null, other has val, not same tree, return F
            return False
        if p.val != q.val: #not null, but the val do not match
            return False
        
        #if the val match, we need to traverse both left and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        

        