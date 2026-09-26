class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        max_use_first = [0 for _ in range(len(nums) - 1)]
        max_use_last = [0 for _ in range(len(nums) - 1)]

        max_use_first[0] = nums[0]
        max_use_first[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            max_use_first[i] = max(max_use_first[i - 1], max_use_first[i - 2] + nums[i])

        max_use_last[0] = nums[1]
        max_use_last[1] = max(nums[1], nums[2])
        for i in range(2, len(nums) - 1):
            max_use_last[i] = max(max_use_last[i - 1], max_use_last[i - 2] + nums[i + 1])
        
        return max(max_use_first[-1], max_use_last[-1])
