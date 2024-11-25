# TC: O(NlogN+MlogM); SC: O(N)
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # pair difficulty and profit 
        job_pair = [(difficulty[i], profit[i]) for i in range(len(difficulty))]
        job_pair.sort()
        worker.sort()

        max_profit = 0
        total_profit = 0 
        heap = [] # max_heap
        job_idx = 0

        for w in worker:
            while job_idx < len(difficulty) and job_pair[job_idx][0] <= w:
                heapq.heappush(heap, -job_pair[job_idx][1])
                job_idx += 1
            if heap:
                max_profit = -heap[0]
            total_profit += max_profit

        return total_profit

