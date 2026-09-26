class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k - 1):
            heapq.heappush(heap, (-nums[i], i))
        L = 0
        R = k - 1
        res = []
        while R < len(nums):
            heapq.heappush(heap, (-nums[R], R))
            while heap[0][1] < L:
                heapq.heappop(heap)
            res.append(-heap[0][0])
            L += 1
            R += 1
        return res