class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2) 
        dp = []

        for i in range(m+1):
            row = []
            for j in range(n+1):
                row.append(-1)
            dp.append(row)

        def recursive_f(s1, s2):
            if s1 == m or s2 == n:
                return 0
            if dp[s1][s2] != -1:
                return dp[s1][s2]
            if text1[s1] == text2[s2]:
                res = 1 + recursive_f(s1+1, s2+1)
                dp[s1][s2] = res
            else:
                res = max(recursive_f(s1+1,s2), recursive_f(s1,s2+1))
                dp[s1][s2] = res
            return res
        
        result = recursive_f(0,0)
        # print(result)

        # print(dp)
        return result

