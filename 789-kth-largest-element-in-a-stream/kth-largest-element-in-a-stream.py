# TC: contruction: O(n) for heapify; O(logn)for popping, we do it (n-k) times; in worst case k=1; log(nlogn)
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


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)