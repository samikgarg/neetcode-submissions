class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstCol, firstRow = False, False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                firstCol = True
                break
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                firstRow = True
                break
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[i])):
                    matrix[i][j] = 0
        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0
        
        if firstCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if firstRow:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        
        