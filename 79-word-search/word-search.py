class Solution:
    def out_of_bound(self, board: List[List[str]], x: int, y: int)-> bool:
        r , c = len(board), len(board[0])
        if x < 0 or y < 0: # any of the co-ordinate is -1, out_of_bound from left or up
            return True
        if x == r or y == c: # out_of_bound from right and down
            return True
        return False
        
    def dfs(self, board: List[List[str]], x: int, y: int, visited: dict, word: str, idx: int) -> bool:
        if self.out_of_bound(board,x,y):
            return False

        if visited.get((x,y), 0): # checks cycle
            return False

        if board[x][y] != word[idx]:
            return False

        visited[(x, y)] = True

        if idx == len(word)-1:
            return True
        
        up_x, up_y = x-1, y
        down_x, down_y = x+1, y
        left_x, left_y = x, y-1
        right_x, right_y = x, y+1

        res = (self.dfs(board,up_x,up_y,visited,word,idx+1) 
            or self.dfs(board,down_x,down_y,visited,word,idx+1)
            or self.dfs(board,left_x, left_y,visited,word,idx+1)
            or self.dfs(board,right_x, right_y,visited,word,idx+1))

        visited[(x,y)] = False
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = dict()
                res = self.dfs(board, i, j, visited, word, 0)
                if res:
                    return res
        return res
