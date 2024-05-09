class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        max_sum_happiness = 0
        given_k = k

        for h in happiness:
            heapq.heappush(heap, -h)
        
        max_sum_happiness += - (heapq.heappop(heap))
        k -= 1

        while k > 0 and heap:
            turn_took = given_k - k
            top = - (heapq.heappop(heap) + turn_took)
            if top >= 0:
                max_sum_happiness += top
            k -= 1

        return max_sum_happiness