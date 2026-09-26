class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        started = False
        while not started or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            started = True
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            