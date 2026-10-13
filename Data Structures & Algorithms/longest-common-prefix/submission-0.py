class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixIndex = len(strs[0])
        
        for i in range(1, len(strs)):
            currIndex = 0
            while currIndex < len(strs[0]) and currIndex < len(strs[i]) and strs[0][currIndex] == strs[i][currIndex]:
                currIndex += 1
            prefixIndex = min(prefixIndex, currIndex)
        
        return strs[0][:prefixIndex]