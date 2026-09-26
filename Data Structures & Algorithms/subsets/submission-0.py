class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        excludingFirst = self.subsets(nums[1:])
        return excludingFirst + [[nums[0]] + p for p in excludingFirst]
        