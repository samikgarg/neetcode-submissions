class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumArray = sum(nums)

        if target > sumArray or target < -sumArray:
            return 0

        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[len(nums)][0] = 1
        for i in range(len(nums) - 1, -1, -1):
            for currTarget in range(-sumArray, sumArray + 1):
                dp[i][currTarget] += dp[i + 1][currTarget - nums[i]]
                dp[i][currTarget] += dp[i + 1][currTarget + nums[i]]
        
        return dp[0][target]