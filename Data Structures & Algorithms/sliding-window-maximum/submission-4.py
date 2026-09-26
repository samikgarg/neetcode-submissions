class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        values = deque()
        for i in range(k - 1):
            while len(values) > 0 and values[-1][0] < nums[i]:
                values.pop()
            values.append((nums[i], i))
        res = []
        L = 0
        for R in range(k-1, len(nums)):
            while len(values) > 0 and values[-1][0] < nums[R]:
                values.pop()
            values.append((nums[R], R))
            while values[0][1] < L:
                values.popleft()
            res.append(values[0][0])
            L += 1
        return res
            