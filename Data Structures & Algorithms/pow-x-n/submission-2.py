class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(currN):
            if currN == 0:
                return 1
            if currN % 2:
                rest = helper((currN - 1) // 2)
                return x * rest * rest
            rest = helper(currN // 2)
            return rest * rest
        
        res = helper(abs(n))
        return res if n >= 0 else 1/res