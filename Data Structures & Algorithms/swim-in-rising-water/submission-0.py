class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        distTo = [[float("inf")] * len(grid) for _ in range(len(grid))]
        distTo[0][0] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]
        visited = [[False] * len(grid) for _ in range(len(grid))]

        while heap:
            dist, i, j = heapq.heappop(heap)
            if visited[i][j]:
                continue
            visited[i][j] = True

            if i > 0 and max(dist, grid[i - 1][j]) < distTo[i - 1][j]:
                distTo[i - 1][j] = max(dist, grid[i - 1][j])
                heapq.heappush(heap, (max(dist, grid[i - 1][j]), i - 1, j))
            if j > 0 and max(dist, grid[i][j - 1]) < distTo[i][j - 1]:
                distTo[i][j - 1] = max(dist, grid[i][j - 1])
                heapq.heappush(heap, (max(dist, grid[i][j - 1]), i, j - 1))
            if i < len(grid) - 1 and max(dist, grid[i + 1][j]) < distTo[i + 1][j]:
                distTo[i + 1][j] = max(dist, grid[i + 1][j])
                heapq.heappush(heap, (max(dist, grid[i + 1][j]), i + 1, j))
            if j < len(grid) - 1 and max(dist, grid[i][j + 1]) < distTo[i][j + 1]:
                distTo[i][j + 1] = max(dist, grid[i][j + 1])
                heapq.heappush(heap, (max(dist, grid[i][j + 1]), i, j + 1))
        
        return distTo[-1][-1]
