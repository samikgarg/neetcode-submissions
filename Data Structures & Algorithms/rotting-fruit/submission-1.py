class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        diffs = ((1,0), (-1,0), (0,1), (0,-1))
        
        min_minutes = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        while queue:
            i, j, mins = queue.popleft()
            min_minutes = max(mins, min_minutes)
            for di, dj in diffs:
                next_i = i + di 
                next_j = j + dj
                if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) and grid[next_i][next_j] == 1:
                    queue.append((next_i, next_j, mins + 1))
                    grid[next_i][next_j] = -1
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        
        return min_minutes