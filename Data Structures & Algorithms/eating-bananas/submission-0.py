class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isFeasible(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total <= h
        
        low = 1
        high = max(piles)

        while low < high:
            mid = (high + low) // 2
            if isFeasible(mid):
                high = mid
            else:
                low = mid + 1
            
        return low