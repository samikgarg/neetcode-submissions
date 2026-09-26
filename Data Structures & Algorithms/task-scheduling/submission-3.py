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
            heapq.heappush(maxHeap, (-freq[t], t))
        
        queue = deque()
        for t in maxHeap:
            queue.append((-t[0], t[1]))

        totalTime = 0
        while queue:
            currLength = len(queue)
            currCycles = -1
            processed = []
            for i in range(currLength):
                currCycles += 1
                totalTime += 1
                freq, currTask = queue.popleft()
                if freq - 1 > 0:
                    processed.append((freq - 1, currTask))
                if currCycles == n:
                    break
            if queue or processed:
                totalTime += max(n - currCycles, 0)
            maxHeap = []
            for t in processed:
                heapq.heappush(maxHeap, (-t[0], t[1]))
            for t in queue:
                heapq.heappush(maxHeap, (-t[0], t[1]))
                queue = deque()
            for t in maxHeap:
                queue.append((-t[0], t[1]))
        return totalTime

