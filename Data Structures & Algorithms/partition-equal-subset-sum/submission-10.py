class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        if sumNums % 2:
            return False

        half = sumNums // 2
        dp = [False] * (half + 1)
        dp[0] = True
        
        for i in range(len(nums) - 1, -1, -1):
            for target in range(half, 0, -1):
                if nums[i] <= target:
                    dp[target] = dp[target - nums[i]] or dp[target]

        return dp[half]
