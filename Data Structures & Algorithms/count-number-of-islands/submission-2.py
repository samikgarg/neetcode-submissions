class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ones = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    ones.add((i, j))
        
        numIslands = 0
        def dfs(i, j):
            if (i, j) not in ones or i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            ones.remove((i, j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        while ones:
            numIslands += 1
            i, j = ones.pop()
            ones.add((i, j))
            dfs(i, j)
        
        return numIslands

            