class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        cache = {}
        def helper(i):
            if i >= len(s):
                return True
            if i in cache:
                return cache[i]

            currString = ""
            for j in range(i, len(s)):
                currString += s[j]
                if currString in wordSet:
                    if helper(j + 1):
                        cache[i] = True
                        return True
            cache[i] = False
            return False
        
        return helper(0)