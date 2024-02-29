# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# false
#     level check
#         if level even
#             - elements are even => return false
#             - elements are odd
#                 - elements are not sorted => return false
                    
#         if level odd
#             - elements odd => return false
#             - elemets are even
#                 - elements are not sorted in (reverse = true) manner => return false

from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        new_list = list()

        if root:
            queue.append(root)
        
        level = 0

        while(len(queue) > 0):
            n = len(queue)

            for i in range(n):
                curr = queue.popleft()
                val = curr.val

                if val in new_list:
                    return False
                new_list.append(val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                if level % 2 == 0 and val % 2 == 0:
                    return False
                if level % 2 != 0 and val % 2 != 0:
                    return False
                
                if i == n - 1:
                    if level % 2 == 0:
                        if new_list != sorted(new_list):
                            return False
                    else:
                        if new_list != sorted(new_list, reverse = True):
                            return False
                    new_list = []

            level += 1

        return True



        