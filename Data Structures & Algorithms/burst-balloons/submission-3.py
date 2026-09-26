class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        cache = {}
        def helper(l, r):
            if (l, r) in cache:
                return cache[(l, r)]
            maxVal = 0
            for i in range(l + 1, r):
                maxVal = max(maxVal, helper(l, i) + helper(i, r) + nums[l] * nums[i] * nums[r])
            cache[(l, r)] = maxVal
            return maxVal

        return helper(0, len(nums) - 1)
