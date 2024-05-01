class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result_mat = list()

        for j in range(len(matrix[0])): #col
            temp = []
            for i in range(len(matrix)): #row
                temp.append(matrix[i][j])
            result_mat.append(temp)
        
        return result_mat
