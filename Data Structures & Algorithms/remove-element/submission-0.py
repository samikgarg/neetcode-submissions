class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        editIndex = 0
        for i in range(len(nums)):
            nums[editIndex] = nums[i]
            if nums[i] != val:
                editIndex += 1
        return editIndex