class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        candidates.sort()

        res = []
        prev = -1
        for i, c in enumerate(candidates):
            if c == prev:
                continue
            if c > target:
                return res
            if c == target:
                res.append([c])
                return res
            res.extend([c] + rest for rest in self.combinationSum2(candidates[i + 1:], target - c))
            prev = c

        return res