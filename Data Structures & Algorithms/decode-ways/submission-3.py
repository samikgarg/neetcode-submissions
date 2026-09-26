class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) > 0 and s[0] == '0':
            return 0
        
        if s == "" or len(s) == 1:
            return 1
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return self.numDecodings(s[1:]) + self.numDecodings(s[2:] if int(s[:2]) <= 26 else "0")