"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        line = defaultdict(int)
        for interval in intervals:
            line[interval.start] += 1
            line[interval.end] -= 1
        
        maxDays = 0
        days = 0
        for point in sorted(line.keys()):
            days += line[point]
            maxDays = max(days, maxDays)
        
        return maxDays


