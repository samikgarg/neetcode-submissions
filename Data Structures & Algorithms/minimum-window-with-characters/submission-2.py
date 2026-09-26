class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for c in t:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        start = -1
        for i, c in enumerate(s):
            if c in freq:
                start = i
                break
        
        if start == -1:
            return ""

        L = start
        min_str = s[:] + "A"
        curr_freq = {}
        for c in freq:
            curr_freq[c] = 0

        def check_equal(curr_freq, freq):
            for c in freq:
                if curr_freq[c] < freq[c]:
                    return False
            return True
        
        found = []
        for R in range(L, len(s)):
            if s[R] in curr_freq:
                curr_freq[s[R]] += 1
                if R != start:
                    found.append(R)
            while check_equal(curr_freq, freq):
                if R - L < len(min_str):
                    min_str = s[L:R+1]
                if len(found) > 0:
                    curr_freq[s[L]] -= 1
                    L = found.pop(0)
                else:
                    break
        
        if len(min_str) > len(s):
            return ""
        else:
            return min_str


        