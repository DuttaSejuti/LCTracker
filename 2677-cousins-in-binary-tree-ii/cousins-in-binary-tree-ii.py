# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelSums = []
        queue = deque()

        queue.append(root) # least node size is 1, no need to check not root

        # traversing the tree to get the level sums, except for level 0 and level 1
        level = 0
        while len(queue) > 0:
            level_sum = 0
            for i in range(len(queue)):
                curr = queue.popleft()
                level_sum += curr.val
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            # if level == 0 or level == 1:
            #     levelSums.append(0)
            # else:
            levelSums.append(level_sum)
            level += 1
        levelSums.append(0)
        # traversing tree to replace the node value to it's cousins
        root.val = 0
        queue.append(root) # least node size is 1, no need to check not root
        # print(levelSums)
        
        level = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                sibling_sum = 0
                curr = queue.popleft()
                
                if curr.left:
                    queue.append(curr.left)
                    sibling_sum += curr.left.val
                if curr.right:
                    queue.append(curr.right)
                    sibling_sum += curr.right.val
                
                level_sum = levelSums[level + 1]
        
                if curr.left: curr.left.val = level_sum - sibling_sum
                if curr.right: curr.right.val = level_sum - sibling_sum

            level += 1
        return root
      