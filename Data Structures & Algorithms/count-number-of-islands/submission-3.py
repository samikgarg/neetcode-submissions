class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        unvisited_ones = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    unvisited_ones.add((i, j))
        
        def dfs(i, j):
            if not(0 <= i < len(grid)) or not(0 <= j < len(grid[0])) or (i, j) not in unvisited_ones:
                return
            unvisited_ones.remove((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        while unvisited_ones:
            count += 1
            i, j = next(iter(unvisited_ones))
            dfs(i, j)
        
        return count