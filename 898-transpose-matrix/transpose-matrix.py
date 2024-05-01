class Solution:
    # def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # result_mat = list()
        # for j in range(len(matrix[0])): #col
        #     temp = []
        #     for i in range(len(matrix)): #row
        #         temp.append(matrix[i][j])
        #     result_mat.append(temp)
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        result_mat = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                result_mat[j][i] = matrix[i][j]
        return result_mat
