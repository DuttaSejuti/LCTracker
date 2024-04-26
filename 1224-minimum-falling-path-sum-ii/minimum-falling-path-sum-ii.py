class Solution:
    def dfs(self, r: int, c: int, matrix: List[List[int]], dp: dict) -> int:
        if r == len(matrix) - 1:
            return matrix[r][c]
        
        if dp[r][c] != -10000000000:
            return dp[r][c]

        min_sum = inf
        column_size = len(matrix[0])
        for col in range(column_size):
            dr, dc = r+1, col
            if c != col:
                min_sum = min(min_sum, matrix[r][c] + self.dfs(dr, dc, matrix, dp))
                
        dp[r][c] = min_sum

        return min_sum

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        min_sum = float(inf)
        dp = [[-10000000000] * (col + 5) for _ in range(row)]

        for j in range(col):
            return_sum = self.dfs(0, j, matrix, dp)
            min_sum = min(min_sum, return_sum)
        
        return min_sum
