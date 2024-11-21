# O(m*n + g(m+n))
class Solution:
    def createGrid(self, rows: int, columns: int) -> List[List[int]]:
        return [[1] * columns for _ in range(rows)]
    
    def outOfBound(self, m: int, n: int, x: int, y: int)-> bool:
        if x < 0 or y < 0: # any of the co-ordinate is -1, out_of_bound from left or up
            return True
        if x == m or y == n: # out_of_bound from right and down
            return True
        return False
    
    def markTheGrid(self, r: int, c: int, grid: List[List[int]]) -> None:
        # directions = [[-1,0],[1,0], [0,-1], [0,1]] # up, down, left, right
        m, n = len(grid), len(grid[0])

        # going up
        dr, dc = r + (-1), c + 0
        if not self.outOfBound(m, n, dr, dc):
            for new_r in range(dr, -1, -1):
                if grid[new_r][dc] == 2 or grid[new_r][dc] == 3: # already wall or a guard
                    break
                grid[new_r][dc] = 4

        # going down
        dr, dc = r + 1, c + 0
        if not self.outOfBound(m, n, dr, dc):
            for new_r in range(dr, m):
                if grid[new_r][dc] == 2 or grid[new_r][dc] == 3:
                    break
                grid[new_r][dc] = 4

        # going left
        dr, dc = r + 0, c + (-1)
        if not self.outOfBound(m, n, dr, dc):
            for new_c in range(dc, -1, -1):
                if grid[dr][new_c] == 2 or grid[dr][new_c] == 3:
                    break
                grid[dr][new_c] = 4

        # going right
        dr, dc = r + 0, c + 1
        if not self.outOfBound(m, n, dr, dc):
            for new_c in range(dc, n):
                if grid[dr][new_c] == 2 or grid[dr][new_c] == 3:
                    break
                grid[dr][new_c] = 4
    
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        unguarded_cell = 0
        grid = self.createGrid(m, n)

        # mark the walls; optimized than traversing the whole matrix and find a wall to mark
        for wall in walls:
            i, j = wall
            grid[i][j] = 2
            
        # mark the guards
        for guard in guards:
            i, j = guard
            grid[i][j] = 3
        
        # traverse guards
        for guard in guards:
            self.markTheGrid(guard[0], guard[1], grid)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    unguarded_cell += 1
            
        return unguarded_cell

# TC: O(m*n + g(m+n)) => TLE
# class Solution:
#     def createGrid(self, rows: int, columns: int) -> List[List[int]]:
#         matrix = []
#         for r in range(rows):
#             temp = []
#             for c in range(columns):
#                 temp.append(1)
#             matrix.append(temp)
#         return matrix
    
#     def outOfBound(self, m: int, n: int, x: int, y: int)-> bool:
#         if x < 0 or y < 0: # any of the co-ordinate is -1, out_of_bound from left or up
#             return True
#         if x == m or y == n: # out_of_bound from right and down
#             return True
#         return False

#     def markTheGrid(self, grid: List[List[int]], r: int, c: int, wall_set: Set[Tuple[int, int]], marked_cell: int) -> int:
#         # directions = [[-1,0],[1,0], [0,-1], [0,1]] # up, down, left, right
#         m, n = len(grid), len(grid[0])

#         # going up
#         dr, dc = r + (-1), c + 0
#         if not self.outOfBound(m, n, dr, dc):
#             for new_r in range(dr, -1, -1):
#                 if (new_r, dc) in wall_set:
#                     if grid[new_r][dc] != 0:
#                         grid[new_r][dc] = 0
#                         marked_cell += 1
#                     break
#                 if grid[new_r][dc] == 0: # already guarded, not breaking cause, we might have cells that we have not visited
#                     continue
#                 grid[new_r][dc] = 0
#                 marked_cell += 1

#         # going down
#         dr, dc = r + 1, c + 0
#         if not self.outOfBound(m, n, dr, dc):
#             for new_r in range(dr, m):
#                 if (new_r, dc) in wall_set:
#                     if grid[new_r][dc] != 0:
#                         grid[new_r][dc] = 0
#                         marked_cell += 1
#                     break
#                 if grid[new_r][dc] == 0: # already guarded or a wall
#                     continue
#                 grid[new_r][dc] = 0
#                 marked_cell += 1

#         # going left
#         dr, dc = r + 0, c + (-1)
#         if not self.outOfBound(m, n, dr, dc):
#             for new_c in range(dc, -1, -1):
#                 if (dr, new_c) in wall_set:
#                     if grid[dr][new_c] != 0:
#                         grid[dr][new_c] = 0
#                         marked_cell += 1
#                     break
#                 if grid[dr][new_c] == 0:
#                     continue
#                 grid[dr][new_c] = 0
#                 marked_cell += 1

#         # going right
#         dr, dc = r + 0, c + 1
#         if not self.outOfBound(m, n, dr, dc):
#             for new_c in range(dc, n):
#                 if (dr, new_c) in wall_set:
#                     if grid[dr][new_c] != 0:
#                         grid[dr][new_c] = 0
#                         marked_cell += 1
#                     break
#                 if grid[dr][new_c] == 0:
#                     continue
#                 grid[dr][new_c] = 0
#                 marked_cell += 1

#         return marked_cell

#     def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
#         total_cell = m * n
#         marked_cell = 0
#         guard_set = set(tuple(guard) for guard in guards)
#         wall_set = set(tuple(wall) for wall in walls)

#         grid = self.createGrid(m, n)

#         for i in range(m):
#             for j in range(n):
#                 if (i, j) in wall_set and grid[i][j] != 0:
#                     grid[i][j] = 0
#                     marked_cell += 1
#                     continue
#                 if (i, j) in guard_set:
#                     if grid[i][j] != 0:
#                         grid[i][j] = 0
#                         marked_cell += 1
#                     marked_cell = self.markTheGrid(grid, i, j, wall_set, marked_cell)

#         return total_cell - marked_cell
