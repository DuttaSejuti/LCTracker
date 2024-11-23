# 1) we will convert the rows to columns
# 2) for 90 degree rotation, the first row becomes the last column, and the last row becomes the first column
# 3) before converting we need to modify each row
#   i) count the no of stones, if get a obstacle, the stones till now encountered will be upon the obstacle
#  ii) if we reach the end and there is still stones count, this means we did not encounter any obstable in the path,
#     the stones will go to the bottom

# TC: O(M*N) => even though we have a while loop inside a nested loop, the values are only processed once.
# its total work is bounded by n
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        gem_count = 0
        new_box = [] # modified rows

        # modifying the rows
        for row in box:
            new_row = ['.']*len(row)
            for i in range(len(row)):
                if row[i] == '#':
                    gem_count += 1

                # if we find a obstacle, the stones encountered till now will be above it
                if row[i] == '*': # if we encounter a obstacle
                    new_row[i] = '*' # obstacles place will be unchanged
                    j = i - 1
                    while gem_count >= 1:
                        new_row[j] = '#'
                        gem_count -= 1
                        j -= 1
                # to handle, when there are no obstables scenario
                if i == len(row)-1 and gem_count >= 1:
                    j = i
                    while gem_count >= 1:
                        new_row[j] = '#'
                        gem_count -= 1
                        j -= 1

            gem_count = 0
            new_box.append(new_row)
        
        # construct the skeleton of the result matrix, no row of rows become column, no of columns become rows
        m, n = len(box[0]), len(box)
        result_box = [['.']*n for _ in range(m)]

        # convert the modified rows into columns inversely
        for i in range(len(new_box)-1, -1, -1):
            row = new_box[i]
            c = len(new_box) - (i+1)
            for r in range(len(row)):
                result_box[r][c] = row[r]
        
        return result_box
