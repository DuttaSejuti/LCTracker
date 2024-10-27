# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes_max_height = dict()
        self.node_level = dict() # node 5: level 3
        self.level_first_max_height = dict()
        self.level_second_max_height = dict()

    def dfs(self, root: Optional[TreeNode], level: int) -> int:
        if root is None:
            return 0

        res = max(self.dfs(root.left, level+1) + 1, self.dfs(root.right, level+1) + 1)
        self.nodes_max_height[root.val] = res
        self.node_level[root.val] = level

        if res >= self.level_first_max_height.get(level, 0):
            self.level_second_max_height[level] = self.level_first_max_height.get(level, 0)
            self.level_first_max_height[level] = res
        else:
            self.level_second_max_height[level] = max(self.level_second_max_height.get(level, 0), res)

        return res
    
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        max_height = self.dfs(root, 1)
        result_height = []

        for query in queries:
            deleted_node_max_height = self.nodes_max_height[query]
            deleted_node_level = self.node_level[query]
            first_max, second_max = self.level_first_max_height.get(deleted_node_level, 0), self.level_second_max_height.get(deleted_node_level, 0)
            
            if deleted_node_max_height == first_max:
                updated_height = max_height - deleted_node_max_height + second_max
                result_height.append(updated_height-1) #i have computed. 1 indexed level
            else:
                result_height.append(max_height-1)
        return result_height
        