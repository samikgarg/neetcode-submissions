class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProductTails = [0] * len(nums)
        maxProductTails[0] = (nums[0], nums[0])

        for i in range(1, len(nums)):
            minPrev, maxPrev = maxProductTails[i - 1]
            currMin = min(nums[i], minPrev * nums[i], maxPrev * nums[i])
            currMax = max(nums[i], minPrev * nums[i], maxPrev * nums[i])
            maxProductTails[i] = (currMin, currMax)
        
        return max(maxProductTails, key = lambda el : el[1])[1]