class Solution:
    # used max-heap => as only positive value will be present in the array.
    # TC: O(n + klogn), SC:O(n)
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        max_sum_happiness = 0
        given_k = k

        # populate the heap as max-heap, max value on top, O(n)
        for h in happiness:
            heapq.heappush(heap, -h)
        

        # till we have k and heap, simulate
        while k > 0 and heap:
            # as we need to decrease the rest of the values, after each turn, rather then decreasing all after each turn
            # we can simply just consider how many turn has taken place, and decrement it from the popped value
            turn_took = given_k - k
            top = - (heapq.heappop(heap) + turn_took) # pop takes O(logn), happening k times => O(klogn) 

            if top >= 0:
                max_sum_happiness += top
            k -= 1

        return max_sum_happiness
