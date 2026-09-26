class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(index):
            if index == len(candidates):
                return []
            res = []
            prev = -1
            for i in range(index, len(candidates)):
                c = candidates[i]
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

        return backtrack(0)