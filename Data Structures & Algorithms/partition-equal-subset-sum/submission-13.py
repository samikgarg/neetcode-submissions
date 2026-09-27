class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False
        
        sum_needed = nums_sum // 2
        sum_possible = [False] * (sum_needed + 1)
        sum_possible[0] = True
        
        for num in nums:
            for i in range(sum_needed, num - 1, -1):
                if num <= i and sum_possible[i - num]:
                    sum_possible[i] = True
        
        return sum_possible[sum_needed]

