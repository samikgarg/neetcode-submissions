class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def equalTo(si, pi):
            if si >= len(s) or pi >= len(p):
                return False
            return s[si] == p[pi] or p[pi] == "."
        
        dp = [False] * (len(p) + 1)
        for si in range(len(s), -1, -1):
            prev = dp[len(p)]
            dp[len(p)] = si == len(s)
            for pi in range(len(p) - 1, -1, -1):
                temp = dp[pi]
                if pi < len(p) - 1 and p[pi + 1] == '*':
                    dp[pi] = (equalTo(si, pi) and dp[pi]) or dp[pi + 2] 
                else:
                    dp[pi] = equalTo(si, pi) and prev
                prev = temp
        return dp[0]

    

