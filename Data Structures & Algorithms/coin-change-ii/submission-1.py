class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        next, curr = [0] * (amount + 1), [0] * (amount + 1)

        for i in range(len(coins) - 1, -1, -1):
            curr[0] = 1
            for currAmount in range(1, amount + 1):
                curr[currAmount] = next[currAmount]
                if coins[i] <= currAmount:
                    curr[currAmount] += curr[currAmount - coins[i]]
            next, curr = curr, next
        
        return next[amount]