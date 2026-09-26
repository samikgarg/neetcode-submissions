class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1] * n
        currRow = [0] * n
        for i in range(m - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    currRow[j] += prevRow[j]
                if j < n - 1:
                    currRow[j] += currRow[j + 1]
            prevRow, currRow = currRow, [0] * n
        return prevRow[0]