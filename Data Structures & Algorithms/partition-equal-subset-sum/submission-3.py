class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)

        if sumNums % 2:
            return False
        
        half = sumNums // 2
        
        cache = {}
        def helper(target, index):
            if target == 0:
                return True
            if (target, index) in cache:
                return cache[(target, index)]
            if index >= len(nums) or target < 0:
                return False
            for i in range (index, len(nums)):
                if nums[i] > target:
                    continue
                if helper(target - nums[i], i + 1):
                    cache[(target, index)] = True
                    return True
            cache[(target, index)] = False
            return False
        
        return helper(half, 0)
