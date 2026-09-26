class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        def helper(index, isBought, buyVal):
            if index >= len(prices):
                return 0
            
            if isBought:
                if prices[index] <= buyVal:
                    return helper(index + 1, True, prices[index])
                return max(prices[index] - buyVal + helper(index + 2, False, 0), helper(index + 1, True, buyVal))
            return helper(index + 1, True, prices[index])
        
        return helper(0, False, 0)