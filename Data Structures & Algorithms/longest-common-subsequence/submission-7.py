class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text1) + 1)
        
        for i in range(1, len(text2) + 1):
            prev = 0
            for j in range(1, len(text1) + 1):
                temp = dp[j]
                if text1[j - 1] != text2[i - 1]:
                    dp[j] = max(dp[j], dp[j - 1])
                else:
                    dp[j] = 1 + prev
                prev = temp
        
        return dp[-1]
