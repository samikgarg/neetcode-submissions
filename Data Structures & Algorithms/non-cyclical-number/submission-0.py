class Solution:
    def isHappy(self, n: int) -> bool:
        def sumDigitsSquares(num):
            res = 0
            while num:
                res += (num % 10) ** 2
                num //= 10
            return res
        
        slow = n
        fast = sumDigitsSquares(n)
        while fast != 1:
            if fast == slow:
                return False
            slow = sumDigitsSquares(slow)
            fast = sumDigitsSquares(sumDigitsSquares(fast))
        return True