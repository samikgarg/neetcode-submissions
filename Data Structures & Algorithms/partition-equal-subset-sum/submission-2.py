class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)

        if sumNums % 2:
            return False
        
        half = sumNums // 2

        def helper(target, index):
            if target == 0:
                return True
            if index >= len(nums) or target < 0:
                return False
            for i in range (index, len(nums)):
                if nums[i] > target:
                    continue
                if helper(target - nums[i], i + 1):
                    return True
            return False
        
        return helper(half, 0)
