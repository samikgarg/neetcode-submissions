class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        def helper(index, isBought):
            if index >= len(prices):
                return 0
            
            if isBought:
                return max(helper(index + 2, False) + prices[index], helper(index + 1, True))
            return max(helper(index + 1, True) - prices[index], helper(index + 1, False))
        
        return helper(0, False)