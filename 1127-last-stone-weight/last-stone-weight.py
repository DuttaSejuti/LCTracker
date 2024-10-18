# Brute Force Sol
# TC: O(n*nlogn); we are performing sorting (nlogn) for n times
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         if len(stones)==1:
#             return stones[0]
#         while 1:
#             stones.sort(reverse = True)
#             first_stone = stones[0]
#             second_stone = stones[1]
#             if(first_stone == second_stone):
#                 if( len(stones) == 2):
#                     return int(0)
#                 else:
#                     del stones[0:2]
#             else:
#                 stones[0] = first_stone - second_stone
#                 stones.remove(second_stone)
#             if len(stones) == 1:
#                 return stones[0]

# Optimal solution
# TC: O(nlogn) using maxHeap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # for single value, we do not create a heap at all
        if len(stones) == 1:
            return stones[0]
        
        # constructing max heap
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        # as we need at least 2 values in the heap to perform the operations
        # or you can check while len(maxHeap) > 1
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
