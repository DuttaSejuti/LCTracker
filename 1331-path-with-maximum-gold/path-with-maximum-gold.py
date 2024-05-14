class Solution:
    def out_of_bound(self, i: int, j: int, grid: List[List[int]]) -> bool:
        row, col = len(grid), len(grid[0])
        if i < 0 or j < 0 or i == row or j == col:
            return True
        return False
    
    def dfs(self, i: int, j: int, grid: List[List[int]], visited: dict) -> int:
        if self.out_of_bound(i, j, grid):
            return 0
        
        if visited.get((i, j)) != None:
            return 0
        
        if grid[i][j] == 0:
            return 0
        
        visited[(i, j)] = 1

        directions = [[-1,0],[1,0], [0,-1], [0,1]] #up, down, left, right
        max_gold = 0
            
        for direction in directions:
            dr, dc = i + direction[0], j + direction[1]
            max_gold = max(max_gold, grid[i][j] + self.dfs(dr, dc, grid, visited))

        visited.pop((i, j))
        return max_gold

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        max_gold = 0

        for i in range(r):
            for j in range(c):
                visited = {}
                max_gold = max(max_gold, self.dfs(i, j, grid, visited))

        return max_gold
