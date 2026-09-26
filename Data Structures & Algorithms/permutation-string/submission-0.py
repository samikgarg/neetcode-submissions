class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        chars = 'abcdefghijklmnopqrstuvwxyz'
        freq = {}
        curr_freq = {}
        L = 0
        R = len(s1) - 1

        for c in chars:
            freq[c] = 0
            curr_freq[c] = 0

        for i, c in enumerate(s1):
            freq[c] += 1
            curr_freq[s2[i]] += 1
        
        while R < len(s2):
            if curr_freq == freq:
                return True
            curr_freq[s2[L]] -= 1
            L += 1
            R += 1
            if R < len(s2):
                curr_freq[s2[R]] += 1
        
        return False
            
