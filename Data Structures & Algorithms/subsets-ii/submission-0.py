class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def backtrack(index):
            if index >= len(nums):
                return [[]]
            currNum = nums[index]
            duplicates = 0
            for i in range(index, len(nums)):
                if nums[i] == currNum:
                    duplicates += 1
                else:
                    break
            currSets = []
            for i in range(duplicates + 1):
                currSets.append([currNum for _ in range(i)])
            restSets = backtrack(index + duplicates)

            res = []
            for curr in currSets:
                for rest in restSets:
                    res.append(curr + rest)
            return res
        
        return backtrack(0)
            
