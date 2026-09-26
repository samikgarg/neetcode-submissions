class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        res = []
        for i, num in enumerate(nums):
            res.extend([[num] + per for per in self.permute(nums[:i] + nums[i + 1:])])
        return res