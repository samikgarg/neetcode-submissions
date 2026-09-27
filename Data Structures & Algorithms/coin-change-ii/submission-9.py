class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        combos = [0] * (amount + 1)
        combos[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                combos[i] += combos[i - coin]
        
        return combos[amount]
        