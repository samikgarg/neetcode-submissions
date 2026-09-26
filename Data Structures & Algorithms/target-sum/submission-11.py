class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumArray = sum(nums)

        if target > sumArray or target < -sumArray or (target + sumArray) % 2:
            return 0
        
        subsetSum = (target + sumArray) // 2
        dp = [0] * (subsetSum + 1)
        dp[0] = 1

        for num in nums:
            for currSum in range(subsetSum, num - 1, -1):
                dp[currSum] += dp[currSum - num]
        
        return dp[subsetSum]