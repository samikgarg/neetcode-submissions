class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []
        edge = 0
        currDir = 0
        start = (0, 0)
        i, j = (0, 1) if len(matrix[0]) > 1 else (1, 0) 
        while edge < len(matrix) - edge and edge < len(matrix[0]) - edge:
            res.append(matrix[edge][edge])
            dirIndex = 0
            while (i, j) != start and edge <= i < len(matrix) - edge and edge <= j < len(matrix[0]) - edge:
                res.append(matrix[i][j])
                if not(edge <= i + dirs[currDir][0] < len(matrix) - edge and edge <= j + dirs[currDir][1] < len(matrix[0]) - edge):
                    currDir += 1
                i, j = i + dirs[currDir][0], j + dirs[currDir][1]
            edge += 1
            start = (edge, edge)
            i, j = (edge, edge + 1) if len(matrix[0]) - 2 * edge > 1 else (edge + 1, edge)
            currDir = 0
        return res

