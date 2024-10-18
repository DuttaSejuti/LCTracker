# we are maintsining minHeap of size k
#  removing the min values from the heap till len(heap) > k
#  will make sure the kth largest value is in the top
# same kind of problem like kth largest element in stream: https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
# TC: O(nlogk); SC: O(k); minheap of size k
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
    
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

# Can be solved with maxHeap, but TC and SC both will be costly
# TC: O(n+logk); SC: O(n)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         max_heap = [-num for num in nums]
#         heapq.heapify(max_heap)
    
#         # Extract the maximum element k times
#         for _ in range(k):
#             kth_largest = -heapq.heappop(max_heap)
    
#         return kth_largest
