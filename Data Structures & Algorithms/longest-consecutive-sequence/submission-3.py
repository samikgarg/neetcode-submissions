class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        numsSet = set(nums)
        starts = []
        maxLength = 1
        for num in nums:
            if num - 1 not in numsSet:
                starts.append(num)
        for start in starts:
            curr = start
            currLength = 1
            while curr + 1 in numsSet:
               currLength += 1 
               curr += 1
            maxLength = max(maxLength, currLength)
        return maxLength
            

        