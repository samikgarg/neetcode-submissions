class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] + (-prices[j] + dp[j - 2])
        if len(prices) <= 1:
            return 0

        dp = [0] * len(prices)
        dp[0] = 0
        dp[1] = max(0, prices[1] - prices[0])
        max_profit = max(-prices[0], -prices[1])
        for i in range(2, len(prices)):
            max_profit = max(max_profit, -prices[i] + dp[i - 2])
            dp[i] = max(prices[i] + max_profit, dp[i - 1])
        
        return dp[-1]