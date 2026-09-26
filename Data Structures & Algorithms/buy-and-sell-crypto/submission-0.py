class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1

        maxProfit = 0
        while (R < len(prices)):
            maxProfit = max(maxProfit, prices[R] - prices[L])
            if (prices[L] > prices[R]):
                L = R
            R += 1
        
        return maxProfit
        