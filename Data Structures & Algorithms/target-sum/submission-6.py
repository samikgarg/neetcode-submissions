class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumArray = sum(nums)

        if target > sumArray or target < -sumArray:
            return 0

        nextDP, currDP = defaultdict(int), defaultdict(int)
        nextDP[0] = 1
        for i in range(len(nums) - 1, -1, -1):
            for currTarget in range(-sumArray, sumArray + 1):
                currDP[currTarget] = nextDP[currTarget - nums[i]] + nextDP[currTarget + nums[i]]
            nextDP, currDP = currDP, nextDP
        
        return nextDP[target]