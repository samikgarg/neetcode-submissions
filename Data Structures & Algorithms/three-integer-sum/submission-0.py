class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def twoSum(target, index):
            L = index + 1
            R = len(nums) - 1
            found = set()
            while R > L:
                if nums[L] + nums[R] == target:
                    curr_group = [-target, nums[L], nums[R]]
                    curr_group.sort()
                    found.add(tuple(curr_group))
                    L += 1
                    R -= 1
                elif nums[L] + nums[R] < target:
                    L += 1
                else:
                    R -= 1
            return list(found)
        
        groups = set()
        for i, num in enumerate(nums):
            groups.update(twoSum(-num, i))
        
        return [list(group) for group in groups]
        