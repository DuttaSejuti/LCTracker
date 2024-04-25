class Solution:
    # recursion with dp
    # parameters => position, prev char
    # choice => pick current char, do not pick current char
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [[-1] * 30 for _ in range(len(s))]

        def recursion(i, prev):
            if i == len(s):
                return 0
            
            if dp[i][prev] != -1:
                return dp[i][prev]

            dp[i][prev] = 0

            res = recursion(i+1, prev) # proceed but do not pick s[i]

            if prev == 28 or abs((ord(s[i]) - ord('a')) - prev) <= k:
                res = max(res, 1 + recursion(i+1, (ord(s[i]) - ord('a')))) # proceed and pick s[i],
            
            dp[i][prev] = res

            return res
    
        return recursion(0, 28)