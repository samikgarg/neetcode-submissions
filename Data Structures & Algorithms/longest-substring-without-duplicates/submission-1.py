class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        found = {}
        maxLength = 1
        currStart = 0
        for i, c in enumerate(s):
            if c in found:
                currStart = max(currStart, found[c] + 1)

            found[c] = i
            maxLength = max(i - currStart + 1, maxLength)

        return maxLength