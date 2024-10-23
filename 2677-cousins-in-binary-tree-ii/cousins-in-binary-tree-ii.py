# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # 2 Pass BFS
# class Solution:
#     def generateLevelSum(self, root: Optional[TreeNode]) -> List[int]:
#         levelSums = []
#         queue = deque()

#         queue.append(root) # least node size is 1, no need to check not root

#         # traversing the tree to get the level sums, except for level 0 and level 1
#         level = 0
#         while len(queue) > 0:
#             level_sum = 0
#             for i in range(len(queue)):
#                 curr = queue.popleft()
#                 level_sum += curr.val
#                 if curr.left: queue.append(curr.left)
#                 if curr.right: queue.append(curr.right)
#             levelSums.append(level_sum)
#             level += 1

#         return levelSums

#     def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         levelSums = self.generateLevelSum(root)

#         levelSums.append(0) # as we are accessing level 2's sum in level 1,
#         # we need to append a dummy 0 to avoid out of bound error

#         # traversing tree to replace the node value to it's cousins
#         queue = deque()
#         root.val = 0 # at level 0, root will always be 0, as it does not have any sibling, hence no cousin
#         queue.append(root) # least node size is 1, no need to check not root
        
#         level = 0
#         while len(queue) > 0:
#             for i in range(len(queue)):
#                 sibling_sum = 0
#                 curr = queue.popleft()
                
#                 if curr.left:
#                     queue.append(curr.left)
#                     sibling_sum += curr.left.val
#                 if curr.right:
#                     queue.append(curr.right)
#                     sibling_sum += curr.right.val
                
#                 level_sum = levelSums[level + 1]
        
#                 if curr.left: curr.left.val = level_sum - sibling_sum
#                 if curr.right: curr.right.val = level_sum - sibling_sum

#             level += 1
#         return root
      

# 1 pass BFS
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # from one level, calculate the next level's level sum and sibling_sum
        # we will update the sibling's node val with it's sibling_sum

        queue = deque()
        queue.append(root)
        level_sum = root.val # at level 0, level_sum will be the root's val itself
        next_level_sum = 0 # we want to know the next level's sum

        while len(queue) > 0:
            next_level_sum = 0
            for i in range(len(queue)):
                curr = queue.popleft()
                curr.val = level_sum - curr.val # here, curr.val will be the sibling sum of that node

                sibling_sum = 0
                if curr.left:
                    sibling_sum += curr.left.val
                    next_level_sum += curr.left.val
                if curr.right:
                    sibling_sum += curr.right.val
                    next_level_sum += curr.right.val
                
                if curr.left:
                    curr.left.val = sibling_sum # updating the node's val with it's sibling sum
                    queue.append(curr.left)
                if curr.right:
                    curr.right.val = sibling_sum
                    queue.append(curr.right)
                
            level_sum = next_level_sum
        return root