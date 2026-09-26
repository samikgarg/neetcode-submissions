class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        dp = [[-1] * len(nums) for _ in range(len(nums))]
        def helper(l, r):
            if dp[l][r] != -1:
                return dp[l][r]
            maxVal = 0
            for i in range(l + 1, r):
                maxVal = max(maxVal, helper(l, i) + helper(i, r) + nums[l] * nums[i] * nums[r])
            dp[l][r] = maxVal
            return maxVal

        return helper(0, len(nums) - 1)
