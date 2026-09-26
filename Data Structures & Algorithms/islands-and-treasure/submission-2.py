class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        diffs = ((1,0), (-1,0), (0,1), (0,-1))
        
        visited = set()
        queue = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            i, j = queue.popleft()
            for di, dj in diffs:
                next_i = i + di
                next_j = j + dj
                if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) and (next_i, next_j) not in visited and grid[next_i][next_j] != -1:
                    grid[next_i][next_j] = min(grid[next_i][next_j], grid[i][j] + 1)
                    queue.append((next_i, next_j))
                    visited.add((next_i, next_j))