class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def equalTo(si, pi):
            if si >= len(s) or pi >= len(p):
                return False
            return s[si] == p[pi] or p[pi] == "."
        
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True
        for si in range(len(s), -1, -1):
            for pi in range(len(p) - 1, -1, -1):
                if pi < len(p) - 1 and p[pi + 1] == '*':
                    dp[si][pi] = dp[si][pi + 2] or (equalTo(si, pi) and dp[si + 1][pi])
                else:
                    dp[si][pi] = equalTo(si, pi) and dp[si + 1][pi + 1]
        return dp[0][0]

    

