class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        new_n = len(grid) - 2
        r, c = len(grid), len(grid[0])
        max_val = float(-inf)

        new_mat = []
        for i in range(new_n):
            temp = [0]*new_n
            new_mat.append(temp)

        for i in range(r-2):
            for j in range(c-2):
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        val = grid[k][l]
                        max_val = max(max_val, val)
                new_mat[i][j] = max_val
                max_val = float(-inf)

        return new_mat
