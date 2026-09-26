class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for i1 in range(len(word1)):
            dp[len(word2)][i1] = len(word1) - i1
        for i2 in range(len(word2)):
            dp[i2][len(word1)] = len(word2) - i2
        
        for i2 in range(len(word2) - 1, -1, -1):
            for i1 in range(len(word1) - 1, -1, -1):
                if word1[i1] == word2[i2]:
                    dp[i2][i1] = dp[i2 + 1][i1 + 1]
                else:
                    dp[i2][i1] = 1 + min(dp[i2 + 1][i1 + 1], dp[i2][i1 + 1], dp[i2 + 1][i1])
        return dp[0][0]