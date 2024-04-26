class Solution:
    def in_bound(self, r: int, c:int, matrix: List[List[int]]) -> bool:
        row, col = len(matrix), len(matrix[0])

        if (r >= 0 and c >= 0) and (r < row and c < col):
            return True
        return False

    def dfs(self, r: int, c: int, matrix: List[List[int]], dp: dict) -> int:
        if r == len(matrix) - 1:
            return matrix[r][c]
        
        if (r,c) in dp:
            return dp[(r,c)]

        directions = [[1,0],[1,-1],[1,1]]
        min_sum = float(inf)

        for direction in directions:
            dr, dc = r+direction[0], c+direction[1]
            if self.in_bound(dr, dc, matrix):
                min_sum = min(min_sum, matrix[r][c] + self.dfs(dr, dc, matrix, dp))
                
        dp[(r,c)] = min_sum

        return min_sum

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        min_sum = float(inf)
        dp = {}

        for j in range(col):
            return_sum = self.dfs(0, j, matrix, dp)
            min_sum = min(min_sum, return_sum)
        
        return min_sum