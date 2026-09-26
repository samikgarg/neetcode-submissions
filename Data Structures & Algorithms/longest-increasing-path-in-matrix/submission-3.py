class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        notVisited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                notVisited.add((i, j))
        
        maxVal = [1]
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            res = 1
            dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for dx, dy in dirs:
                if 0 <= i + dx < len(matrix) and 0 <= j + dy < len(matrix[0]) and matrix[i + dx][j + dy] > matrix[i][j]:
                    res = max(res, 1 + dfs(i + dx, j + dy))
            memo[(i, j)] = res
            maxVal[0] = max(maxVal[0], res)
            notVisited.remove((i, j))
            return res
        
        while notVisited:
            i, j = next(iter(notVisited))
            dfs(i, j)
        
        return maxVal[0]
        
        
        