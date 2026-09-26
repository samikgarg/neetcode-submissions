class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] >= nums[0]:
                low = mid + 1
            else:
                high = mid - 1

        return nums[0]