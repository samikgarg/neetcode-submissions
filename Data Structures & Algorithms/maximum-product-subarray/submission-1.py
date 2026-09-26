class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]

        currMinProduct = nums[0]
        currMaxProduct = nums[0]
        for i in range(1, len(nums)):
            currMin = min([nums[i], nums[i] * currMinProduct, nums[i] * currMaxProduct])
            currMax = max([nums[i], nums[i] * currMinProduct, nums[i] * currMaxProduct])
            currMinProduct, currMaxProduct = currMin, currMax
            maxProduct = max(maxProduct, currMaxProduct)
        
        return maxProduct