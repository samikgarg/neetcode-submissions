class MedianFinder:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.median = []

    def addNum(self, num: int) -> None:
        if len(self.median) < 2 and not(self.minHeap or self.maxHeap):
            self.median.append(num)
        elif len(self.median) == 2:
            self.median.append(num)
            self.median.sort()
            heapq.heappush(self.maxHeap, -self.median.pop(0))
            heapq.heappush(self.minHeap, self.median.pop())
        else:
            if num >= self.median[0]:
                heapq.heappush(self.minHeap, num)
                self.median.append(heapq.heappop(self.minHeap))
            else:
                heapq.heappush(self.maxHeap, -num)
                self.median.append(-heapq.heappop(self.maxHeap))
        self.median.sort()

    def findMedian(self) -> float:
        if len(self.median) == 1:
            return self.median[0]
        else:
            return (self.median[0] + self.median[1]) / 2
        