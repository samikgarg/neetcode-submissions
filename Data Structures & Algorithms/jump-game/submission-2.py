class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            for num in range(min(nums[i] + 1, len(nums) - i)):
                if dp[i + num]:
                    dp[i] = True
        return dp[0]