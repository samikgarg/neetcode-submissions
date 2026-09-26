class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = nums[:]
        if len(nums) > 2:
            dp[2] = nums[2] + dp[0]

        for i in range(3, len(nums)): 
            dp[i] = nums[i] + max(dp[i - 2], dp[i - 3])
        
        return max(dp[-1], dp[-2])
        