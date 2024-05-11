class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio_quality_pair = list()

        # creating ratio, quality pair list
        for i in range(len(quality)):
            ratio = wage[i]/quality[i]
            ratio_quality_pair.append((ratio, quality[i]))
        
        ratio_quality_pair.sort()

        # heap => will maintain a max-heap
        heap = []
        quality_sum = 0
        min_cost = float(inf)

        # we want to have minimum cost, 
        for i in range(len(quality)):
            curr_ratio = ratio_quality_pair[i][0]
            curr_quality = ratio_quality_pair[i][1]

            heapq.heappush(heap, -curr_quality)
            quality_sum += curr_quality

            if len(heap) > k:
                top = heapq.heappop(heap)
                quality_sum -= -top
            
            if len(heap) == k:
                min_cost = min(min_cost, quality_sum*curr_ratio)
            
        return min_cost
