class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        plusOneFalse, plusTwoFalse, plusOneTrue = 0, 0, 0

        for i in range(len(prices) - 1, -1, -1):
            plusOneFalse, plusTwoFalse, plusOneTrue = max(plusOneTrue - prices[i], plusOneFalse), plusOneFalse, max(plusTwoFalse + prices[i], plusOneTrue)
        
        return plusOneFalse