class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumArray = sum(nums)

        if target > sumArray or target < -sumArray or (target + sumArray) % 2:
            return 0
        
        subsetSum = (target + sumArray) // 2
        dp = [[0] * (subsetSum + 1) for _ in range(len(nums) + 1)]
        dp[len(nums)][0] = 1

        for i in range(len(nums) - 1, -1, -1):
            for currSum in range(subsetSum + 1):
                dp[i][currSum] = dp[i + 1][currSum]
                if currSum >= nums[i]:
                    dp[i][currSum] += dp[i + 1][currSum - nums[i]]

        
        return dp[0][subsetSum]