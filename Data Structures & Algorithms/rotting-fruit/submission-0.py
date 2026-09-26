class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = set()
        rotten = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2: 
                    queue.append((0, i, j))
                    rotten.add((i, j))
                if grid[i][j] == 1:
                    fresh.add((i, j))
        
        maxTime = 0
        while queue:
            currTime, i, j = queue.popleft()
            if (i, j) not in fresh and (i, j) not in rotten:
                continue
            maxTime = max(maxTime, currTime)
            if (i, j) in fresh:
                fresh.remove((i, j))
            if (i, j) in rotten:
                rotten.remove((i, j))
            queue.append((currTime + 1, i + 1, j))
            queue.append((currTime + 1, i - 1, j))
            queue.append((currTime + 1, i, j + 1))
            queue.append((currTime + 1, i, j - 1))
        
        if fresh:
            return -1
        return maxTime
