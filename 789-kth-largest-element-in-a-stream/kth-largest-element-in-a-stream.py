# TC: contruction: O(n) for heapify; O(logn)for popping, we do it (n-k) times; in worst case k=1; log(nlogn)
#     add: O(mlogn)
# SC: O(n); size of the heap
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # we want minHeap of size K; after popping the rest of the min values, we will
        # end up having k largest values in the heap, minHeap trick, instead of maxHeap
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # our initial heap can have less than k elements, then we do not want to pop the element
        # we only pop if our heap size gets greater than k adter adding new val
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # 0 index in the minHeap contains the smallest value of the heap
        return self.heap[0]

# without heapify
# class KthLargest:
#     def __init__(self, k: int, nums: List[int]):
#         self.min_heap = []
#         self.k = k

#         for num in nums:
#             self.add(num)

#     def add(self, val: int) -> int:
#         # Add to our min_heap if we haven't processed k elements yet
#         # or if val is greater than the top element (the k-th largest)
#         if len(self.min_heap) < self.k or self.min_heap[0] < val:
#             heapq.heappush(self.min_heap, val)
#             if len(self.min_heap) > self.k:
#                 heapq.heappop(self.min_heap)
#         return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)