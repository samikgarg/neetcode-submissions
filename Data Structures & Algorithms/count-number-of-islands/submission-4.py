class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        unvisited_ones = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    unvisited_ones.add((i, j))

        queue = deque()
        while unvisited_ones:
            count += 1
            i, j = next(iter(unvisited_ones))
            queue.append((i, j))
            while queue:
                i, j = queue.popleft()
                if not(0 <= i < len(grid)) or not(0 <= j < len(grid[i])) or (i,j) not in unvisited_ones:
                    continue
                unvisited_ones.remove((i, j))
                queue.append((i + 1, j))
                queue.append((i - 1, j))
                queue.append((i, j + 1))
                queue.append((i, j - 1))
        
        return count
