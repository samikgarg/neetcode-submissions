class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        queue = deque()
        for i in range(len(heights)):
            queue.append((i, 0))
        for i in range(len(heights[0])):
            queue.append((0, i))
        
        foundPacific = set()
        while queue:
            i, j = queue.popleft()
            if ((i, j)) in foundPacific:
                continue
            foundPacific.add((i, j))
            if i > 0 and heights[i - 1][j] >= heights[i][j]:
                queue.append((i - 1, j))
            if j < len(heights[0]) - 1 and heights[i][j + 1] >= heights[i][j]:
                queue.append((i, j + 1))
            if j > 0 and heights[i][j - 1] >= heights[i][j]:
                queue.append((i, j - 1))
            if i < len(heights) - 1 and heights[i + 1][j] >= heights[i][j]:
                queue.append((i + 1, j))
        
        res = []
        queue = deque()
        foundAtlantic = set()
        for i in range(len(heights)):
            queue.append((i, len(heights[0]) - 1))
        for i in range(len(heights[0])):
            queue.append((len(heights) - 1, i))
        while queue:
            i, j = queue.popleft()
            if ((i, j)) in foundAtlantic:
                continue
            foundAtlantic.add((i, j))
            if (i, j) in foundPacific:
                res.append([i, j])
            if i > 0 and heights[i - 1][j] >= heights[i][j]:
                queue.append((i - 1, j))
            if j < len(heights[0]) - 1 and heights[i][j + 1] >= heights[i][j]:
                queue.append((i, j + 1))
            if j > 0 and heights[i][j - 1] >= heights[i][j]:
                queue.append((i, j - 1))
            if i < len(heights) - 1 and heights[i + 1][j] >= heights[i][j]:
                queue.append((i + 1, j))
        
        return res


        
            
            