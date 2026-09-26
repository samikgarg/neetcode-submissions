class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for i in range(len(coins) - 1, -1, -1):
            dp[i][0] = 1
            for currAmount in range(1, amount + 1):
                dp[i][currAmount] = dp[i + 1][currAmount]
                if coins[i] <= currAmount:
                    dp[i][currAmount] += dp[i][currAmount - coins[i]]
        
        return dp[0][amount]