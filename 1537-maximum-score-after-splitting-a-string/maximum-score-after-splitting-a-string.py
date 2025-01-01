class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        zero_count, one_count = 0, 0

        for i in range(len(s)-1):
            if s[i] == '0':
                zero_count += 1
            for j in range(i+1, len(s)):
                if s[j] == '1':
                    one_count += 1
            max_score = max(max_score, zero_count + one_count)
            one_count = 0
        
        return max_score
