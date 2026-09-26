class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        
        nextDP, currDP = [[False] * (len(s1) + 1)], [False] * (len(s1) + 1)

        currDP[len(s1)] = True
        for i2 in range(len(s2), -1, -1):
            for i1 in range(len(s1), -1, -1):
                if i2 < len(s2) and s2[i2] == s3[i1 + i2]:
                    currDP[i1] = nextDP[i1]
                if i1 < len(s1) and s1[i1] == s3[i1 + i2]:
                    currDP[i1] = currDP[i1] or currDP[i1 + 1]
            nextDP, currDP = currDP, [False] * (len(s1) + 1)
        
        return nextDP[0]