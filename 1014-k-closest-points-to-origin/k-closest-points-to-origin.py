class Solution:
    def calculateDistance(self, point: List[int]):
        x1, y1 = 0, 0 # origin
        x2, y2 = point[0], point[1]
        eu_distance = math.sqrt(pow((x1-x2), 2) + pow((y1-y2), 2)) # you can omit doing sqrt

        return eu_distance

    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     minHeap = []
    #     result = []
    #     for point in points:
    #         distance = self.calculateDistance(point)
    #         heapq.heappush(minHeap, (distance, point)) # tuple => (distance, [co-ordinate])
        
    #     while k:
    #         res = heapq.heappop(minHeap)
    #         result.append(res[1]) # append the co-ordinate
    #         k -= 1
        
    #     return result

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        result = []
        for point in points:
            distance = self.calculateDistance(point)
            minHeap.append((distance, point))

        heapq.heapify(minHeap)
        
        while k:
            res = heapq.heappop(minHeap)
            result.append(res[1]) # append the co-ordinate
            k -= 1
            
        return result
