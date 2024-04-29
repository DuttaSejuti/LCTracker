class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        result = 0
        row_record = dict()
        col_record = dict()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    row_record[i] = row_record.get(i, 0) + 1
                    col_record[j] = col_record.get(j, 0) + 1

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    result += (row_record[i]-1)*(col_record[j]-1)
                                                 
        return result
