class Solution:
    # def tribonacci(self, n: int) -> int:
    #     dp = [-1] * 38
    #     if n == 0:
    #         return 0
    #     if n == 1 or n == 2:
    #         return 1
        
    #     return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

    # def createFibonacciOf38(self)-> List:
    #     f = [0 , 1]

    #     for i in range(2, 38):
    #         f.append(f[i-1] + f[i-2])
        
    #     return f

    def tribonacci(self, n: int) -> int:
        f = [0, 1, 1]

        for i in range(3, 38, 1):
            f.append(f[i-3] + f[i-2] + f[i-1])
        
        return f[n]
