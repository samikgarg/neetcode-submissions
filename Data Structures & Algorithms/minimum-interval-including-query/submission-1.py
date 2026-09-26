class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        indices = {q : [] for q in queries}
        for i, q in enumerate(queries):
            indices[q].append(i)
        
        res = [-1] * len(queries)
        queries = list(set(queries))
        intervals.sort()
        queries.sort()
        heap = []
        intervalIndex = 0
        for q in queries:
            while intervalIndex < len(intervals) and intervals[intervalIndex][0] <= q:
                heapq.heappush(heap, Interval(intervals[intervalIndex]))
                intervalIndex += 1
            while heap and heap[0].end < q:
                heapq.heappop(heap)
            if heap:
                for i in indices[q]:
                    res[i] = heap[0].end - heap[0].start + 1
        return res



class Interval:
    def __init__(self, lst):
        self.start = lst[0]
        self.end = lst[1]
    
    def __lt__(self, other):
        return self.end - self.start < other.end - other.start