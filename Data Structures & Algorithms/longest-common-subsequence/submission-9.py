class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0] * len(text2) for _ in range(len(text1))]

        found = False
        for i in range(len(text1)):
            if text1[i] == text2[0]:
                found = True
            if found:
                dp[i][0] = 1
        
        found = False
        for j in range(len(text2)):
            if text1[0] == text2[j]:
                found = True
            if found:
                dp[0][j] = 1

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])
        
        return dp[-1][-1]

