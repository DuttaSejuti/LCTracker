class Solution:
    def out_of_bound(self, grid: List[List[str]], r: int, c:int) -> bool:
        row = len(grid)
        column = len(grid[0])

        if r == row or c == column:
            return True
        if r < 0 or c < 0:
            return True
        return False

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        r, c = len(grid), len(grid[0])

        for i in range(r):
            for j in range(c):
                r_up, c_up = i-1, j
                r_down, c_down = i+1, j
                r_left, c_left = i, j-1
                r_right, c_right = i, j+1

                if grid[i][j] == 1:
                    # for up cell
                    if not self.out_of_bound(grid, r_up, c_up):
                        if grid[r_up][c_up] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1

                    # for down cell
                    if not self.out_of_bound(grid, r_down, c_down):
                        if grid[r_down][c_down] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1

                    # for left cell
                    if not self.out_of_bound(grid, r_left, c_left):
                        if grid[r_left][c_left] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1

                    # for right cell
                    if not self.out_of_bound(grid, r_right, c_right):
                        if grid[r_right][c_right] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1

        return perimeter
                    