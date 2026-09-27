class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        cache = {}
        def helper(si, ti):
            if (si, ti) in cache:
                return cache[(si, ti)]
            
            if ti == len(t):
                return 1
            if si == len(s):
                return 0
            
            num = 0
            if s[si] == t[ti]:
                num += helper(si + 1, ti + 1)
            num += helper(si + 1, ti)

            cache[(si, ti)] = num
            return num
        
        return helper(0, 0)