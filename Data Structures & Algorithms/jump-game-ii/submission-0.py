class Solution:
    def jump(self, nums: List[int]) -> int:
        currEnd = 0
        nextEnd = 0
        steps = 0
        for start in range(len(nums)):
            if currEnd >= len(nums) - 1:
                break
            nextEnd = max(nextEnd, nums[start] + start)
            if start == currEnd:
                currEnd = nextEnd
                steps += 1

        return steps