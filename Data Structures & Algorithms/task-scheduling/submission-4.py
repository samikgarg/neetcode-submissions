class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks:
            if t in freq:
                freq[t] += 1
            else:
                freq[t] = 1
        
        maxHeap = []
        for t in freq:
            heapq.heappush(maxHeap, -freq[t])
        
        queue = deque()
        totalTime = 0
        while queue or maxHeap:
            totalTime += 1
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                if freq + 1 < 0:
                    queue.append((freq + 1, totalTime + n))
            
            if queue and queue[0][1] == totalTime:
                heapq.heappush(maxHeap, queue.popleft()[0])

            
        return totalTime

