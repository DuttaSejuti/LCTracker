class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        ranked_scores = sorted(scores, reverse = True)
        result = []

        for score in scores:
            idx = ranked_scores.index(score)
            if idx == 0:
                result.append('Gold Medal')
            elif idx == 1:
                result.append('Silver Medal')
            elif idx == 2:
                result.append('Bronze Medal')
            else:
                result.append(str(idx+1))
            
        return result
