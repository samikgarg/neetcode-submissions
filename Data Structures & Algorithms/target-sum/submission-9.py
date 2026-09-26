class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumArray = sum(nums)

        if target > sumArray or target < -sumArray or (target + sumArray) % 2:
            return 0
        
        subsetSum = (target + sumArray) // 2
        def helper(i, currSum):
            if i >= len(nums) and currSum == 0:
                return 1
            if i >= len(nums):
                return 0
            return helper(i + 1, currSum) + helper(i + 1, currSum - nums[i])

        #dp = [0] * (len(nums) + 1)
        #dp[0] = 1

        
        return helper(0, subsetSum)