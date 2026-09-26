class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            currMin = float("inf")
            for coin in coins:
                if coin > i:
                    break
                currMin = min(currMin, 1 + dp[i - coin])
            dp[i] = currMin

        return -1 if dp[amount] == float("inf") else dp[amount]