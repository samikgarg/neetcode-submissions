class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            for num in range(nums[i] + 1):
                if i + num < len(nums) and dp[i + num]:
                    dp[i] = True
        return dp[0]