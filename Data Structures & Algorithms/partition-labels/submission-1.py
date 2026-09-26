class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        start = -1
        end = 0
        for i, c in enumerate(s):
            end = max(end, lastIndex[c])
            if i == end:
                res.append(end - start)
                start = i
            
        return res