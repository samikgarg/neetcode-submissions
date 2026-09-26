class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        cache = {}
        def helper(i1, i2):
            i3 = i1 + i2
            if i1 == len(s1) and i2 == len(s2):
                return True
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            elif i1 < len(s1) and i2 < len(s2) and s1[i1] == s3[i3] and s2[i2] == s3[i3]:
                res = helper(i1 + 1, i2) or helper(i1, i2 + 1)
            elif i1 < len(s1) and s1 and s1[i1] == s3[i3]:
                res = helper(i1 + 1, i2)
            elif i2 < len(s2) and s2 and s2[i2] == s3[i3]:
                res = helper(i1, i2 + 1)
            else:
                res = False
            cache[(i1, i2)] = res
            return res
        
        return helper(0, 0)