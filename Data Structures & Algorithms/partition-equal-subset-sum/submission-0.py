class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)

        if sumNums % 2:
            return False
        
        half = sumNums // 2
        #dp = [False for _ in range(target + 1)]

        def helper(target, excluded):
            if target == 0:
                return True
            for i, num in enumerate(nums):
                if num > target or i in excluded:
                    continue
                added = False
                if i not in excluded:
                    added = True
                    excluded.add(i)
                if helper(target - num, excluded):
                    return True
                if added:
                    excluded.remove(i)
            return False
        
        return helper(half, set())
