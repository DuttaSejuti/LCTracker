class Solution:
    def inBound(self, r: int, c: int, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])

        if (r >= 0 and c >= 0) and (r < row and c < col):
            return True
        return False
    
    def dfs(self, r: int, c: int, grid: List[List[int]], dp: dict) -> int:
        if not self.inBound(r, c, grid):
            return 0
        
        if (r,c) in dp:
            return dp[(r,c)]

        directions = [[-1,1],[0,1],[1,1]]
        max_move = 0

        for direction in directions:
            dr, dc = r + direction[0], c + direction[1]
            if self.inBound(dr, dc, grid) and grid[r][c] < grid[dr][dc]:
                max_move = max(max_move, 1 + self.dfs(dr, dc, grid, dp))
        
        dp[(r,c)] = max_move
    
        return max_move


    def maxMoves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = {}
        max_move = 0 # to compare with the result val to get max

        # as the row value will be change here, column will always start at 0
        for i in range(row):
            return_move = self.dfs(i, 0, grid, dp)
            max_move = max(max_move, return_move)

        return max_move
