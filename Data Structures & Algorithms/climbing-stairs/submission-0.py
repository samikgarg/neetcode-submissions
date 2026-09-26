class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n in Solution.cache:
            return Solution.cache[n]
        res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        Solution.cache[n] = res
        return res