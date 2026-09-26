class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def helper(i, currTarget):
            if i == len(nums) and currTarget == 0:
                return 1
            if i >= len(nums):
                return 0
            if (i, currTarget) in cache:
                return cache[(i, currTarget)]
            res = helper(i + 1, currTarget - nums[i]) + helper(i + 1, currTarget + nums[i])
            cache[(i, currTarget)] = res
            return res
        
        return helper(0, target)