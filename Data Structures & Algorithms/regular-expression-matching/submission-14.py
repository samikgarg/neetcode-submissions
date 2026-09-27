class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}
        def helper(si, pi):
            if (si, pi) in cache:
                return cache[(si, pi)]
            
            if si == len(s) and (pi == len(p) or (pi == len(p) - 2 and p[pi + 1] == "*")):
                return True
            if si == len(s) or pi == len(p):
                return False

            res = False
            if s[si] == p[pi]:
                res = res or helper(si + 1, pi + 1)

            if p[pi] == ".":
                res = res or helper(si + 1, pi + 1) 
            
            if pi < len(p) - 1 and p[pi + 1] == "*":
                res = res or helper(si, pi + 2)
                if p[pi] == "." or p[pi] == s[si]:
                    res = res or helper(si + 1, pi)
                    res = res or helper(si + 1, pi + 2)
            
            cache[(si, pi)] = res
            return res
        
        return helper(0, 0)