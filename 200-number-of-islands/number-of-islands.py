class Solution:
    def out_of_bound(self, grid: List[List[str]], i: int, j:int) -> bool:
        row = len(grid)
        column = len(grid[0])

        if i == row or j == column:
            return True
        if i < 0 or j < 0:
            return True
        return False

    def dfs(self, grid: List[List[str]], visited: set,i: int, j: int) -> None:
        if self.out_of_bound(grid, i, j):
            return

        if grid[i][j] == '0':
            return
    
        if (i,j) in visited:
            return
        
        visited.add((i,j))

        up_i, up_j = i-1, j
        down_i, down_j = i+1, j
        left_i, left_j = i, j-1
        right_i, right_j = i, j+1

        self.dfs(grid, visited, up_i, up_j)
        self.dfs(grid, visited, down_i, down_j)
        self.dfs(grid, visited, left_i, left_j)
        self.dfs(grid, visited, right_i, right_j)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    # if we get a single 1, then we have an island, dosen't matter
                    # if we have other '1's vertically, horizontally or not
                    count += 1
                    self.dfs(grid, visited, i, j)
         
        return count
        