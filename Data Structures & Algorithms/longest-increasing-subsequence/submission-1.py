from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [nums[0]]
        for i in range(1, len(nums)):
            currIndex = bisect_left(tails, nums[i])

            if currIndex == len(tails):
                tails.append(nums[i])
            else:
                tails[currIndex] = nums[i]
        
        return len(tails)

