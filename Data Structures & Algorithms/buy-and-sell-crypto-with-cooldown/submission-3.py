class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        dp = [[0, 0] for _ in range(len(prices) + 2)]

        for i in range(len(prices) - 1, -1, -1):
            dp[i][1] = max(dp[i + 2][0] + prices[i], dp[i + 1][1])
            dp[i][0] = max(dp[i + 1][1] - prices[i], dp[i + 1][0])
        
        return dp[0][0]