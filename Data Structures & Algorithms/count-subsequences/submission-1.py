class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(t)] = 1
        for si in range(len(s) - 1, -1, -1):
            dp[si][len(t)] = 1
            for ti in range(len(t) - 1, -1, -1):
                dp[si][ti] = dp[si + 1][ti]
                if s[si] == t[ti]:
                    dp[si][ti] += dp[si + 1][ti + 1]
        return dp[0][0]
