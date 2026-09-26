class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        sign = abs(x) // x
        x = abs(x)
        
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
            if res > 2**31 - 1:
                return 0
        return sign * res