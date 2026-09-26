class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = {q : -1 for q in queries}
        intervals.sort()
        heap = []
        intervalIndex = 0
        for q in sorted(queries):
            while intervalIndex < len(intervals) and intervals[intervalIndex][0] <= q:
                heapq.heappush(heap, (intervals[intervalIndex][1] - intervals[intervalIndex][0] + 1, intervals[intervalIndex][1]))
                intervalIndex += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[q] = heap[0][0]
        return [res[q] for q in queries]
