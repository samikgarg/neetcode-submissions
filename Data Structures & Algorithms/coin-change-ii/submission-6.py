class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for currAmount in range(1, amount + 1):
                if coin <= currAmount:
                    dp[currAmount] += dp[currAmount - coin]
        
        return dp[amount]