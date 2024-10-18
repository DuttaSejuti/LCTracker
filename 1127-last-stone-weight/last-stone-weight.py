class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # for single value, we do not create a heap at all
        if len(stones) == 1:
            return stones[0]
        
        # constructing max heap
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        # as we need at least 2 values in the heap to perform the operations
        while len(maxHeap) >= 2:
            first_max = - (heapq.heappop(maxHeap))
            second_max = - (heapq.heappop(maxHeap))

            if first_max != second_max:
                heapq.heappush(maxHeap, -(first_max - second_max))

        # if after performing the operations we have an empty heap
        if len(maxHeap) < 1:
            return 0

        # otherwise we have a single value
        return - (maxHeap[0])
