class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        cache = {}
        def helper(i1, i2):
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            
            if i1 == len(s1):
                res = s2[i2:] == s3[i1+i2:]
                cache[(i1, i2)] = res
                return res
            
            if i2 == len(s2):
                res = s1[i1:] == s3[i1 + i2:]
                cache[(i1, i2)] = res
                return res
            
            res = False
            res = res or (s1[i1] == s3[i1+i2] and helper(i1 + 1, i2))
            res = res or (s2[i2] == s3[i1+i2] and helper(i1, i2 + 1))

            cache[(i1, i2)] = res
            return res
        
        return helper(0, 0)

