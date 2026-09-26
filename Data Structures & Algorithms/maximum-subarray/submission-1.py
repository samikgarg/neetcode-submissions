class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sumVal = nums[0]
        for i in range(1, len(nums)):
            sumVal = max(nums[i], sumVal + nums[i])
            maxSum = max(maxSum, sumVal)
        return maxSum