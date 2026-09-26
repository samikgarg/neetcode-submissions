class Solution:
    cache = {}
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        if tuple(nums) in Solution.cache:
            return Solution.cache[tuple(nums)]

        res = []
        for i, num in enumerate(nums):
            res.extend([[num] + per for per in self.permute(nums[:i] + nums[i + 1:])])
        Solution.cache[tuple(nums)] = res
        return res