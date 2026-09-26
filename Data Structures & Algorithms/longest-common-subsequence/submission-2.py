class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            text1, text2 = text2, text1

        cache = {}
        def helper(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if text1[i] != text2[j]:
                res = max(helper(i + 1, j), helper(i, j + 1)) 
            else:
                res = 1 + helper(i + 1, j + 1)
            
            cache[(i, j)] = res
            return res
        
        return helper(0, 0)
        

        
        
        """
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(i, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        

        return dp[len(text1)][len(text2)]
        """
