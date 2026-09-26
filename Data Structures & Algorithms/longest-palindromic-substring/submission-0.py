class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i, c in enumerate(s):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            if len(s[l : r + 1]) > len(longest):
                longest = s[l : r + 1]

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1 
            l += 1
            r -= 1
            if len(s[l : r + 1]) > len(longest):
                longest = s[l : r + 1]

        return longest