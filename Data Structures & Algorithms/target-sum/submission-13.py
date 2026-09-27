class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        def helper(curr_target, curr_index):
            if (curr_target, curr_index) in cache:
                return cache[(curr_target, curr_index)]
            
            if curr_index == -1 and curr_target == 0:
                return 1
            
            if curr_index == -1:
                return 0
            
            res = helper(curr_target - nums[curr_index], curr_index - 1)
            res += helper(curr_target + nums[curr_index], curr_index - 1)

            cache[(curr_target, curr_index)] = res
            return res
        
        return helper(target, len(nums) - 1)