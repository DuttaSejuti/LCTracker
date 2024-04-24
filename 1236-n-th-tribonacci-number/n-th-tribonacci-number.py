class Solution:
    def computation(self, n: int, dp: list) -> int:
        if n in dp:
            res = dp[n]

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            res = computation(n-1) + computation(n-2) + computation(n-3)
            dp[n] = res

        return res

    def tribonacci(self, n: int) -> int:
        dp = [0]*38

        return self.computation(n, dp)

    # TLE
    # def tribonacci(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     if n == 1 or n == 2:
    #         return 1
        
    #     return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

    # got AC
    def tribonacci(self, n: int) -> int:
        f = [0, 1, 1]

        for i in range(3, 38, 1):
            f.append(f[i-3] + f[i-2] + f[i-1])
        
        return f[n]
