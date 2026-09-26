class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __lt__(self, other):
            return math.sqrt(self.x**2 + self.y**2) > math.sqrt(other.x**2 + other.y**2)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap, Point(point[0], point[1]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[point.x, point.y] for point in heap]
            