class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        prevLast, currLast = nums[1], max(nums[1], nums[2])
        for i in range(3, len(nums)):
            prevLast, currLast = currLast, max(currLast, nums[i] + prevLast)
        
        prevFirst, currFirst = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            prevFirst, currFirst = currFirst, max(currFirst, nums[i] + prevFirst)
        
        return max(currLast, currFirst)