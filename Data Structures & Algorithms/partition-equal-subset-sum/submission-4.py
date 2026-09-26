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
            
            res = helper(target - nums[index], index + 1) or helper(target, index + 1) 
            cache[(target, index)] = res
            return res
        
        return helper(half, 0)
