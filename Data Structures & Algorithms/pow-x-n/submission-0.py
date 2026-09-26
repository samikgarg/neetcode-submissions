class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(currN):
            if currN == 0:
                return 1
            if currN == 1:
                return x
            if currN == -1:
                return 1/x
            if currN % 2:
                rest = helper((currN - 1) // 2)
                return x * rest * rest
            rest = helper(currN // 2)
            return rest * rest
        
        return helper(n)