class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def helper(si, pi):
            if (si, pi) in memo:
                return memo[(si, pi)]
            if si == len(s) and (pi == len(p) or (pi == len(p) - 1 and p[pi] == '*') or (pi < len(p) - 1 and p[pi + 1] == '*')):
                return True
            if si == len(s) or pi == len(p):
                return False
            if pi < len(p) - 1 and p[pi + 1] == '*':
                res = helper(si, pi + 1)
            elif p[pi] == '.' or s[si] == p[pi]:
                res = helper(si + 1, pi + 1)
            elif p[pi] == '*' and (p[pi - 1] == '.' or s[si] == p[pi - 1]):
                res = helper(si + 1, pi) or helper(si, pi + 1)
            elif p[pi] == '*':
                res = helper(si, pi + 1)
            else:
                res = False
            memo[(si, pi)] = res
            return res
        return helper(0, 0)
