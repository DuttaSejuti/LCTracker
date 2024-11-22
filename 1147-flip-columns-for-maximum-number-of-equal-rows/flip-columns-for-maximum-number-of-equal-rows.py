# 1) pick each row
# 2) count of same rows, inverted rows
# 3) keep track of the maximum count
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        same_rows_count = 0
        inverted_rows_count = 0
        max_rows = 0

        # to compare each row with rest of the rows for checking equal or invert
        # we need to know the frequency count of the rows
        # O(N)
        row_freq = dict()
        for row in matrix:
            new_tuple = tuple(row) # lists are not hashable for dictionary keys
            row_freq[new_tuple] = row_freq.get(new_tuple, 0) + 1
        
        # traverse the row
        # O(M * N)
        for row in matrix:
            same_rows_count = row_freq.get(tuple(row), 0)
            inverted_row = []
            for element in row:
                if element == 0:
                    inverted_row.append(1)
                else:
                    inverted_row.append(0)
            inverted_rows_count = row_freq.get(tuple(inverted_row), 0)
            max_rows = max(max_rows, same_rows_count + inverted_rows_count)
        
        return max_rows
