class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def helper(i1, i2):
            if i1 == len(word1) and i2 == len(word2):
                return 0
            if i1 == len(word1):
                return len(word2) - i2
            if i2 == len(word2):
                return len(word1) - i1
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            if word1[i1] == word2[i2]:
                res = helper(i1 + 1, i2 + 1)
            else:
                res = 1 + min(helper(i1 + 1, i2 + 1), helper(i1, i2 + 1), helper(i1 + 1, i2))
            memo[(i1, i2)] = res
            return res
        return helper(0, 0)