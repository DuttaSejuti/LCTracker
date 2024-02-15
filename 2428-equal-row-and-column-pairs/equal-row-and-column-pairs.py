class Solution:
    def equalPairs(self, grids: List[List[int]]) -> int:
        pairCount = 0
        columns = []
        j = 0

        for i in range(len(grids)):
            temp = []
            for k in range(len(grids)):
                temp.append(grids[k][j])
            columns.append(temp)
            j += 1
  
        print(columns)

        for g in grids:
            row = g
            for column in columns:
                if row == column:
                    pairCount += 1
        return pairCount