class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        diffs = [(1,0), (-1,0), (0,1), (0,-1)]

        distances = [[1] * len(matrix[0]) for _ in range(len(matrix))]
        unvisited = set((i, j) for j in range(len(matrix[0])) for i in range(len(matrix)))
        
        def dfs(i, j):
            if (i, j) not in unvisited:
                return distances[i][j]
            unvisited.remove((i,j))
            
            max_distance = 1
            for di, dj in diffs:
                next_i = i + di
                next_j = j + dj
                if not(0 <= next_i < len(matrix) and 0 <= next_j < len(matrix[0])):
                    continue
                if matrix[next_i][next_j] > matrix[i][j]:
                    max_distance = max(max_distance, 1 + dfs(next_i, next_j))
            distances[i][j] = max_distance
            return max_distance
        
        max_distance = 0
        while unvisited:
            i, j = next(iter(unvisited))
            max_distance = max(max_distance, dfs(i, j))
        
        return max_distance
