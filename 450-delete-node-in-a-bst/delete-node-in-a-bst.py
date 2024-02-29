# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # we are replacing the node that we are supposed to remove, with the lowest number from it's right subtree
        # min value is found in the left
        def findMin(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        if not root:
            return None
        if val > root.val:
            root.right = self.deleteNode(root.right, val)
        elif val < root.val:
            print("1")
            root.left = self.deleteNode(root.left, val)
            print("6")
        else:
            # for case 1: if the node has 1 child
            # if it doesn't have left child, return right child

            if not root.left:
                print("3")
                return root.right

            # if it doesn't have right child, return left child
            elif not root.right:
                return root.left

            # if the node has 2 child, we remove the lowest value from the right subtree
            else:
                print("2")
                minNode = findMin(root.right) # finds the min value
                root.val = minNode.val # replaces the root's value with the min value

                # to ensure no duplication, remove the min value node
                root.right = self.deleteNode(root.right, minNode.val)
                print("4")

        print("5")
        # print(root)
        return root # print("7")

        # the print("1"), print("2") gives an overview of the flow of the code for below testcase
        # root = [5,3,6,2,4,null,7], key = 3
