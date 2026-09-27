class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]
        minPrev, maxPrev = nums[0], nums[0]
        for i in range(1, len(nums)):
            currMin = min(nums[i], minPrev * nums[i], maxPrev * nums[i])
            currMax = max(nums[i], minPrev * nums[i], maxPrev * nums[i])
            minPrev, maxPrev = currMin, currMax
            maxProduct = max(maxProduct, currMax)
        
        return maxProduct