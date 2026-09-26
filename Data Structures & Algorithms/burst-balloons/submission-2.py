class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        cache = {}
        def helper(l, r):
            if (l, r) in cache:
                return cache[(l, r)]
            maxVal = 0
            for i in range(l + 1, r):
                resLeft = helper(l, i)
                resRight = helper(i, r)
                maxVal = max(maxVal, resLeft + resRight + nums[l] * nums[i] * nums[r])
            cache[(l, r)] = maxVal
            return maxVal

        return helper(0, len(nums) - 1)
