class Solution:
    # TC:O(m*n), SC:O(1)
    def out_of_bound(self, r: int, c:int, row: int, col: int) -> bool:
        if r == row or c == col:
            return True
        if r < 0 or c < 0:
            return True
        return False

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        r, c = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]] # up, down, left, right

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    # loop will traverse 4 constant times
                    for direction in directions:
                        # new r, c
                        dr, dc = i+direction[0], j+direction[1]
                        # counting the edges when directed cell is either water or out_of_bound
                        if not self.out_of_bound(dr, dc, r, c):
                            if grid[dr][dc] == 0:
                                perimeter += 1
                        else:
                            # out_of_bound
                            perimeter += 1

        return perimeter
                    