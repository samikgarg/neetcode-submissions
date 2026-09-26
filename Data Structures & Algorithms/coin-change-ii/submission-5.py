class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            for currAmount in range(1, amount + 1):
                if coins[i] <= currAmount:
                    dp[currAmount] += dp[currAmount - coins[i]]
        
        return dp[amount]