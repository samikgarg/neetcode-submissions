class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        diffs = [(1,0), (-1,0), (0,1), (0,-1)]

        dist = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                dist[(i, j)] = float("inf")
        
        dist[(0, 0)] = grid[0][0]
        heap = [(grid[0][0], 0, 0)]
        while heap:
            max_height, i, j = heapq.heappop(heap)

            if dist[(i, j)] < max_height:
                continue
            
            for di, dj in diffs:
                next_i = i + di
                next_j = j + dj
                if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
                    new_dist = max(dist[(i,j)], grid[next_i][next_j])
                    if new_dist < dist[(next_i, next_j)]:
                        dist[(next_i, next_j)] = new_dist
                        heapq.heappush(heap, (new_dist, next_i, next_j))
        
        return dist[(len(grid) - 1, len(grid[0]) - 1)]