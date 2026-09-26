class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min_index():
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (high + low) // 2
                if nums[mid] < nums[mid - 1]:
                    return mid
                elif nums[mid] >= nums[0]:
                    low = mid + 1
                else:
                    high = mid - 1
            return 0
        
        min_index = find_min_index()
        if min_index == 0:
            max_index = len(nums) - 1
        else:
            max_index = min_index - 1

        def rotated_index(index):
            return (index + min_index) % len(nums)

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            index = rotated_index(mid)
            if target == nums[index]:
                return index
            elif target < nums[index]:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        