class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 0 if s[0] == "0" else 1
        
        dp = [0] * len(s)
        dp[-1] = 0 if s[-1] == "0" else 1
        dp[-2] = 0 if s[-2] == "0" else (dp[-1] + (0 if int(s[len(s) - 2 : len(s)]) > 26 else 1))
        for i in range(len(s) - 3, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            dp[i] = dp[i + 1]
            if int(s[i : i + 2]) <= 26:
                dp[i] += dp[i + 2]
        return dp[0]

        
        
