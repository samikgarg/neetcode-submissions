class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            currNum = abs(nums[i])
            if nums[currNum - 1] < 0:
                return currNum
            nums[currNum - 1] = -nums[currNum - 1]
        return -1
            