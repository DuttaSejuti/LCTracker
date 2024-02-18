class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []

        # TC: O(nlogk) k:length of the heap, which is no of ladders
        # SC: O(k)
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if ladders > 0:
                    heappush(min_heap, diff)
                    ladders -= 1
                else:
                    if min_heap and min_heap[0] < diff:
                        val = heappop(min_heap)
                        bricks -= val
                        heappush(min_heap, diff)
                    else:
                        bricks -= diff
                    if bricks < 0:
                        return i

        return len(heights)-1
