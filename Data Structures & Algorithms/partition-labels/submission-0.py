class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        counts = Counter(s)
        found = set()
        start = 0
        for i, c in enumerate(s):
            if c not in found:
                found.add(c)
            counts[c] -= 1
            if counts[c] == 0:
                found.remove(c)
            if not found:
                res.append(i - start + 1)
                start = i + 1
        return res