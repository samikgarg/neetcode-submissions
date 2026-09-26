class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        if sumNums % 2:
            return False

        half = sumNums // 2
        dp = [False] * (half + 1)
        dp[0] = True
        
        for num in nums:
            for target in range(half, num - 1, -1):
                dp[target] = dp[target - num] or dp[target]

        return dp[half]
