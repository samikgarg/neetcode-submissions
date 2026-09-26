class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        
        dp = [[False] * (len(s1) + 1) for _ in range(len(s2) + 1)]

        dp[len(s2)][len(s1)] = True
        for i1 in range(len(s1), -1, -1):
            for i2 in range(len(s2), -1, -1):
                if i1 < len(s1) and s1[i1] == s3[i1 + i2]:
                    dp[i2][i1] = dp[i2][i1] or dp[i2][i1 + 1]
                if i2 < len(s2) and s2[i2] == s3[i1 + i2]:
                    dp[i2][i1] = dp[i2][i1] or dp[i2 + 1][i1]
        
        return dp[0][0]