class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def helper(si, ti):
            if ti == len(t):
                return 1
            if si == len(s):
                return 0
            if (si, ti) in memo:
                return memo[(si, ti)]
            res = helper(si + 1, ti)
            if s[si] == t[ti]:
                res += helper(si + 1, ti + 1)
            memo[(si, ti)] = res
            return res

        return helper(0, 0)