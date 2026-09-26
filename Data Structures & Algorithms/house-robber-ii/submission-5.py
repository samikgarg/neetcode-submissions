class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prev_use_first = nums[0]
        curr_use_first = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            prev_use_first, curr_use_first = curr_use_first, max(curr_use_first, prev_use_first + nums[i])

        prev_use_last = nums[1]
        curr_use_last = max(nums[1], nums[2])
        for i in range(2, len(nums) - 1):
            prev_use_last, curr_use_last = curr_use_last, max(curr_use_last, prev_use_last + nums[i + 1])
        
        return max(curr_use_first, curr_use_last)
