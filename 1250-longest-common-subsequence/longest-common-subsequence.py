class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2) 
        dp = []

        # form the 2D dp array with one extra index in row and column
        for i in range(m+1):
            row = []
            for j in range(n+1):
                row.append(-1)
            dp.append(row)

        def recursive_f(s1, s2):
            #base case, end of either of the strings
            if s1 == m or s2 == n:
                return 0

            #checks if the computation is already done or not, if done then a value exist in the dp already,
            # then just fetch the value from the dp array
            if dp[s1][s2] != -1: 
                return dp[s1][s2]

            # if a match is found, then add +1, and run the function for the later characters
            if text1[s1] == text2[s2]:
                res = 1 + recursive_f(s1+1, s2+1)
                dp[s1][s2] = res

            # otherwise find the max
            else:
                res = max(recursive_f(s1+1,s2), recursive_f(s1,s2+1))
                dp[s1][s2] = res
            
            return res
        
        result = recursive_f(0,0)
        return result

        # dp = list()
        # m = len(text1)
        # n = len(text2)

        # for i in range(m+1):
        #     row = []
        #     for j in range(n+1):
        #         row.append(0)
        #     dp.append(row)
        
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if text1[i-1] == text2[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # return dp[m][n]