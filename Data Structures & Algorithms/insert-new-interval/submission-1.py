from bisect import bisect_left
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = bisect_left(intervals, newInterval)

        while i > 0 and intervals[i - 1][1] >= newInterval[0]:
            newInterval = [intervals[i - 1][0], max(intervals[i - 1][1], newInterval[1])]
            intervals.pop(i - 1)
            i -= 1
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval = [newInterval[0], max(intervals[i][1], newInterval[1])]
            intervals.pop(i)
        intervals.insert(i, newInterval)

        return intervals
