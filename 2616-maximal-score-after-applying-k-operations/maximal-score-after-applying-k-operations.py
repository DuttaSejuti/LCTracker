class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_score = 0
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)

        while k:
            largest_value = - heapq.heappop(max_heap)
            max_score += largest_value
            new_value = ceil(largest_value/3)
            heapq.heappush(max_heap, -new_value)
            k -= 1

        return max_score