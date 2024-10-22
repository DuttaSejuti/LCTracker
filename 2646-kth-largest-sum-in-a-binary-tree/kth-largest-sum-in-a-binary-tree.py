# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def kthLargest(self, sumList: List[int], k: int) -> int:
#         if len(sumList) < k: return -1
#         sumList.sort(reverse=True)
#         return sumList[k-1]

#     def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
#         queue = deque()
#         sum_list = []

#         if not root:
#             return 0
        
#         queue.append(root)
#         while len(queue) > 0:
#             level_sum = 0
#             for i in range(len(queue)):
#                 curr = queue.popleft()
#                 level_sum += curr.val
#                 if curr.left: queue.append(curr.left)
#                 if curr.right: queue.append(curr.right)
#             sum_list.append(level_sum)
        
#         return self.kthLargest(sum_list, k)


# TC: O(logn+logk)
# SC: O(n)
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        minHeap = []

        if not root:
            return 0
        
        queue.append(root)
        while len(queue) > 0:
            level_sum = 0
            for i in range(len(queue)):
                curr = queue.popleft()
                level_sum += curr.val
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            heapq.heappush(minHeap, level_sum)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        if len(minHeap) < k:
            return -1

        return minHeap[0]
