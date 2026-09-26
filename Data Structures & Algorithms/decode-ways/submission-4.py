class Solution:
    cache = {}
    def numDecodings(self, s: str) -> int:
        if s in Solution.cache:
            return Solution.cache[s]

        if len(s) > 0 and s[0] == '0':
            return 0
        
        if s == "" or len(s) == 1:
            return 1
        
        Solution.cache[s] = self.numDecodings(s[1:]) + self.numDecodings(s[2:] if int(s[:2]) <= 26 else "0")
        return Solution.cache[s]