class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtrack(index, currTarget):
            if index == len(candidates):
                return []
            res = []
            prev = -1
            for i in range(index, len(candidates)):
                c = candidates[i]
                if c == prev:
                    continue
                if c > currTarget:
                    return res
                if c == currTarget:
                    res.append([c])
                    return res
                res.extend([c] + rest for rest in backtrack(i + 1, currTarget - c))
                prev = c
            return res

        return backtrack(0, target)