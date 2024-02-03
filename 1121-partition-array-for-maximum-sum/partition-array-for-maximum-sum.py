class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        m = len(arr)
        sub_arr = []
        dp = []

        for _ in range(m+1):
            row = [-1]*(m+1)
            dp.append(row)
        
        def recursive_func(pos:int, rem:int) -> int:
            if dp[pos][rem] != -1:
                return dp[pos][rem]

            taken = k - rem + 1
            max_val = max(arr[pos - taken + 1:pos + 1])
            l = taken

            if pos == m-1:
                return max_val * l

            if rem == 1:
                res = recursive_func(pos+1, k) + (max_val * l)
            else:
                res = max(recursive_func(pos+1, rem-1), recursive_func(pos+1, k) + max_val * l)
            
            dp[pos][rem] = res
            return res

        result = recursive_func(0, k)
        return result
