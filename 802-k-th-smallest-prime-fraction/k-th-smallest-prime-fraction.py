class Solution:
    # max-heap
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                heapq.heappush(heap, (-(arr[i]/arr[j]), (arr[i], arr[j])))

        while len(heap) > k:
            heapq.heappop(heap)

        pair = heapq.heappop(heap)[1]
        res = [pair[0], pair[1]]
        return res
