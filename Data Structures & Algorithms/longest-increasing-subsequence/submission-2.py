class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LISTails = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    LISTails[i] = max(LISTails[i], 1 + LISTails[j])
        return max(LISTails)