class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        cache = {}
        def LCSIndexed(index_1, index_2):
            if index_1 >= len(text1) or index_2 >= len(text2):
                return 0
            
            if (index_1, index_2) in cache:
                return cache[(index_1, index_2)]

            res = max(LCSIndexed(index_1 + 1, index_2), LCSIndexed(index_1, index_2 + 1))

            if text1[index_1] == text2[index_2]:
                res = max(res, 1 + LCSIndexed(index_1 + 1, index_2 + 1))
            
            cache[(index_1, index_2)] = res
            return res
        
        return LCSIndexed(0, 0)