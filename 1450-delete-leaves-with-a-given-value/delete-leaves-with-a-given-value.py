# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
                # Post Order 
                # [1->2->2] => [5->4->2] next_val = dfs(curr.next)
                                    # curr.val = curr.val + next_val
                # dfs(curr, prevValues)
                
                # Pre Order 
                # [1->2->2] => [1,3,5] curr.val = curr.val + prevValues
                # dfs(curr.next, curr.val)

                # dfs(root, 0)
    # def dfs(curr, t):
    #     curr.next = dfs(curr.next, t) # 1 2 

    #     if curr.next is None and curr.val == t:  # last 2
    #         return None

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root, target):
            if not root:
                return None
            
            root.left = dfs(root.left, target)
            root.right = dfs(root.right, target)

            if root.left == None and root.right == None and root.val == target:
                return None

            return root

        new_root = dfs(root, target)
        return new_root
        
        # new_root = dfs(root, target) = 1-3
        # 1.left = dfs(1.left, 2) = None
        # 2.left = dfs(2.left, 2) = None
        # 2.right = dfs(2.right, 2) = None
        # 1.right = dfs(1.right, 2) = 3
        # 3.left = None
        # 3.right = None



        # new_root = dfs(1-2-3, 2)

        # # start -> option 1, 2, 3
        # # ...... hajar hajar branch
        # # tar ager stage
        # # base case
        