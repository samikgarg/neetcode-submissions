class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if target == 0:
            return [[]]
        if target < 0:
            return []
        
        for i, num in enumerate(nums):
            sums = self.combinationSum(nums[i:], target - num)
            res.extend([[num] + lst for lst in sums])
        
        return res