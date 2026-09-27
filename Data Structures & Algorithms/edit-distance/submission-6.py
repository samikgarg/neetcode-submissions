class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        cache = {}
        def minDistanceHelper(i1, i2):
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            
            if i1 == len(word1):
                return len(word2) - i2
            
            if i2 == len(word2):
                return len(word1) - i1
            
            if word1[i1] == word2[i2]:
                return minDistanceHelper(i1 + 1, i2 + 1)
            
            edit = 1 + minDistanceHelper(i1 + 1, i2 + 1)
            insert = 1 + minDistanceHelper(i1, i2 + 1)
            delete = 1 + minDistanceHelper(i1 + 1, i2)

            res = min(edit, insert, delete)
            cache[(i1, i2)] = res
            return res
        
        return minDistanceHelper(0, 0)