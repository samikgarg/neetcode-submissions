class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ones = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ones.add((i, j))
        
        def dfs(i, j):
            if (i, j) not in ones or i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            ones.remove((i, j))
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
        
        maxArea = 0
        while ones:
            i, j = ones.pop()
            ones.add((i, j))
            area = dfs(i, j)
            maxArea = max(maxArea, area)
        
        return maxArea