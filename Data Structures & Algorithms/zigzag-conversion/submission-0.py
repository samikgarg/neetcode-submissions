class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = ""
        for j in range(0, len(s), 2 * numRows - 2):
            res += s[j]

        for i in range(1, numRows - 1):
            visit = 1
            j = i
            while j < len(s):
                res += s[j]
                if visit % 2:
                    j += 2 * (numRows - i) - 2
                else:
                    j += 2 * i
                visit += 1

        for j in range(numRows - 1, len(s), 2 * numRows - 2):
            res += s[j]
        
        return res