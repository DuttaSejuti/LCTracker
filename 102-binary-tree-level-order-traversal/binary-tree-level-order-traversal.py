# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []

        if root:
            queue.append(root)

        while(len(queue) > 0):
            new_list = []
            for i in range(len(queue)):
                v = queue.popleft()
                new_list.append(v.val)
                if v.left:
                    queue.append(v.left)
                if v.right:
                    queue.append(v.right)
            res.append(new_list)
        return res
        