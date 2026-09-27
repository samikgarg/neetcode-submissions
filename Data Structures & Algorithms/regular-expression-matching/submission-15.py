class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}
        def helper(si, pi):
            if (si, pi) in cache:
                return cache[(si, pi)]
            
            if si >= len(s) and pi == len(p):
                return True
            if pi == len(p):
                return False

            res = False
            if si < len(s) and s[si] == p[pi]:
                res = res or helper(si + 1, pi + 1)

            if si < len(s) and p[pi] == ".":
                res = res or helper(si + 1, pi + 1) 
            
            if pi < len(p) - 1 and p[pi + 1] == "*":
                res = res or helper(si, pi + 2)
                if si < len(s) and (p[pi] == "." or p[pi] == s[si]):
                    res = res or helper(si + 1, pi)
            
            cache[(si, pi)] = res
            return res
        
        return helper(0, 0)