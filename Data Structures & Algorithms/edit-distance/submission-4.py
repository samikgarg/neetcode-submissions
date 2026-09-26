class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        
        dp = [0] * (len(word1) + 1)
        for i1 in range(len(dp)):
            dp[i1] = len(word1) - i1
        
        for i2 in range(len(word2) - 1, -1, -1):
            prev = dp[len(word1)]
            dp[len(word1)] = len(word2) - i2
            for i1 in range(len(word1) - 1, -1, -1):
                temp = dp[i1]
                if word1[i1] == word2[i2]:
                    dp[i1] = prev
                else:
                    dp[i1] = 1 + min(prev, dp[i1 + 1], dp[i1])
                prev = temp
        return dp[0]