class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        plusOne, plusTwo = cost[-2], cost[-1]
        for i in range(len(cost) - 3, -1, -1):
            plusOne, plusTwo = cost[i] + min(plusOne, plusTwo), plusOne
        return min(plusOne, plusTwo)