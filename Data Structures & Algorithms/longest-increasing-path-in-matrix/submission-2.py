class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[1] * len(matrix[0]) for _ in range(len(matrix))]
        coords = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                coords.append((i, j))
        coords.sort(key = lambda c : matrix[c[0]][c[1]])

        for i, j in coords:
            dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]
            for (dx, dy) in dirs:
                if 0 <= i + dx < len(matrix) and 0 <= j + dy < len(matrix[0]) and matrix[i][j] > matrix[i + dx][j + dy]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i + dx][j + dy])
        
        maxRes = 1
        for i in range(len(coords) - 1, -1, -1):
            maxRes = max(maxRes, dp[coords[i][0]][coords[i][1]])

        return maxRes