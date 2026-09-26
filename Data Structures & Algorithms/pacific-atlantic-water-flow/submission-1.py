class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        points = set()
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                points.add((i, j))
        
        final = set()
        reachable = {}
        visited = set()
        def dfs(i, j, minHeight):
            if (i, j) in visited:
                return (False, False)
            if i < 0 or j < 0:
                return (True, False)
            if i >= len(heights) or j >= len(heights[0]):
                return (False, True)
            if heights[i][j] > minHeight:
                return (False, False)
            if (i, j) in reachable:
                return reachable[(i, j)]
            
            visited.add((i, j))
            
            up = dfs(i - 1, j, heights[i][j])
            down = dfs(i + 1, j, heights[i][j])
            left = dfs(i, j - 1, heights[i][j])
            right = dfs(i, j + 1, heights[i][j])
            
            res = [False, False]
            if up[0] or down[0] or left[0] or right[0]:
                res[0] = True
            if up[1] or down[1] or left[1] or right[1]:
                res[1] = True
            res = tuple(res)
            points.remove((i, j))
            reachable[(i, j)] = res
            
            if res[0] and res[1]:
                final.add((i, j))
                if i > 0 and heights[i - 1][j] == heights[i][j]:
                    final.add((i - 1, j))
                    reachable[(i - 1, j)] = (True, True)
                if j > 0 and heights[i][j - 1] == heights[i][j]:
                    final.add((i, j - 1))
                    reachable[(i, j - 1)] = (True, True)
                if i < len(heights) - 1 and heights[i + 1][j] == heights[i][j]:
                    final.add((i + 1, j))
                    reachable[(i + 1, j)] = (True, True)
                if j < len(heights[0]) - 1 and heights[i][j + 1] == heights[i][j]:
                    final.add((i, j + 1))
                    reachable[(i, j + 1)] = (True, True)

            visited.remove((i, j))

            return res
        
        while points:
            i, j = points.pop()
            points.add((i, j))
            dfs(i, j, float('inf'))
        return list(final)
            
            