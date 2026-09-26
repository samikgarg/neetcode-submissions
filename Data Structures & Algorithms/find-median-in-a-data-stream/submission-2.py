class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap:
            self.maxHeap.append(-num)
        elif not self.minHeap:
            nums = [num, -self.maxHeap.pop()]
            self.minHeap.append(max(nums))
            self.maxHeap.append(-min(nums))
        elif (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            if num > self.minHeap[0]:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)
        else:
            if num >= -self.maxHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
                heapq.heappush(self.maxHeap, -num)

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
            return -self.maxHeap[0]
        