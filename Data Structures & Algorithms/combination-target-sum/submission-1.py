class Solution:
    cache = {}
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if target == 0:
            return [[]]
        if target < 0:
            return []
        elif (tuple(nums), target) in Solution.cache:
            return Solution.cache[(tuple(nums), target)]
        
        for i, num in enumerate(nums):
            sums = self.combinationSum(nums[i:], target - num)
            res.extend([[num] + lst for lst in sums])
        
        Solution.cache[(tuple(nums), target)] = res
        return res