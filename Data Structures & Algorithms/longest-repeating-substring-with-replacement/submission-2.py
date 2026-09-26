class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k + 1:
            return len(s)
        
        freq = {}
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            freq[c] = 0
        
        max_freq = 1
        max_length = k + 1
        
        L = 0
        for R in range(len(s)):
            freq[s[R]] += 1
            max_freq = max(max_freq, freq[s[R]])
            
            if (R - L + 1) - max_freq > k:
                freq[s[L]] -= 1
                L += 1
            
            max_length = max(max_length, R - L + 1)
        
        return max_length