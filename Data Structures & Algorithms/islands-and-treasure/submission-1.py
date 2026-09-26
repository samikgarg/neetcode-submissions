class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((0, i, j))

        while queue:
            currDist, i, j = queue.popleft()
            if not(0 <= i < len(grid)) or not(0 <= j < len(grid[i])) or currDist > grid[i][j]:
                continue
            grid[i][j] = currDist
            queue.append((currDist + 1, i + 1, j))
            queue.append((currDist + 1, i - 1, j))
            queue.append((currDist + 1, i, j + 1))
            queue.append((currDist + 1, i, j - 1))


        
