class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[len(t)] = 1
        for si in range(len(s) - 1, -1, -1):
            prev = 1
            for ti in range(len(t) - 1, -1, -1):
                temp = dp[ti]
                if s[si] == t[ti]:
                    dp[ti] += prev
                prev = temp
        return dp[0]
