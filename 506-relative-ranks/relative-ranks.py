class Solution:
    # without sorting, but TC:O(nlogn), SC:O(n)
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        heap = []
        for i, score in enumerate(scores):
            heapq.heappush(heap, (-score, i))
        
        res = ['']*len(scores)

        rank = 1
        while heap:
            idx = heapq.heappop(heap)[1]
            if rank == 1:
                res[idx] = 'Gold Medal'
            elif rank == 2:
                res[idx] = 'Silver Medal'
            elif rank == 3:
                res[idx] = 'Bronze Medal'
            else:
                res[idx] = str(rank)
            rank += 1
        
        return res

    # TC:O(nlogn), SC:O(n)
    # def findRelativeRanks(self, scores: List[int]) -> List[str]:
    #     score_idx = dict()

    #     for i in range(len(scores)):
    #         score_idx[scores[i]] = i

    #     scores.sort(reverse=True)
    #     result = ['']*len(scores)

    #     for i in range(len(scores)):
    #         # this uses O(n) to find the idx, use dictionary to access the idx in O(1)
    #         # idx = ranked_scores.index(score)

    #         idx = score_idx[scores[i]]
    #         if i == 0:
    #             result[idx] = 'Gold Medal'
    #         elif i == 1:
    #             result[idx] = 'Silver Medal'
    #         elif i == 2:
    #             result[idx] = 'Bronze Medal'
    #         else:
    #             result[idx] = str(i+1)
            
    #     return result