class Solution:
    def numDecodings(self, s: str) -> int:
        
        def can_decode(substr):
            if substr[0] == "0":
                return False
            if 1 <= int(substr) <= 26:
                return True
        
        num_decodings = [0] * len(s)
        if can_decode(s[0]):
            num_decodings[0] += 1
        if len(s) == 1 and can_decode(s[0]):
            return num_decodings[0]

        if can_decode(s[:2]):
            num_decodings[1] += 1
        if can_decode(s[0]) and can_decode(s[1]):
            num_decodings[1] += 1

        for i in range(2, len(s)):
            if can_decode(s[i - 1 : i + 1]):
                num_decodings[i] += num_decodings[i - 2]
            if can_decode(s[i]):
                num_decodings[i] += num_decodings[i - 1]
        
        return num_decodings[len(s) - 1]
            
        

