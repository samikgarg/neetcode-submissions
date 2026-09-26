class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k + 1:
            return len(s)
        
        freq = {}
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            freq[c] = 0

        L = 0
        R = k

        max_freq = 1
        max_char = s[0]
        max_length = k + 1
        
        for i in range(R + 1):
            freq[s[i]] += 1
            if freq[s[i]] > max_freq:
                    max_freq = freq[s[i]]
                    max_char = s[i]
        
        while R < len(s) - 1:
            R += 1
            freq[s[R]] += 1
            if freq[s[R]] > max_freq:
                    max_freq = freq[s[R]]
                    max_char = s[R]
            
            if (R - L + 1) - max_freq > k:
                freq[s[L]] -= 1
                L += 1
            
            max_length = max(max_length, R - L + 1)
        
        return max_length