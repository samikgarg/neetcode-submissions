class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def equalTo(si, pi):
            if si >= len(s) or pi >= len(p):
                return False
            return s[si] == p[pi] or p[pi] == "."
        
        memo = {}
        def helper(si, pi):
            if (si, pi) in memo:
                return memo[(si, pi)]
            if si == len(s) and pi == len(p):
                return True
            if pi < len(p) - 1 and p[pi + 1] == '*':
                res = helper(si, pi + 2) or (equalTo(si, pi) and helper(si + 1, pi))
            elif equalTo(si, pi):
                res = helper(si + 1, pi + 1)
            else:
                res = False
            memo[(si, pi)] = res
            return res
        return helper(0, 0)
    

