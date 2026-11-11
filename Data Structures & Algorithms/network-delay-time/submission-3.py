class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjacency = [[] for _ in range(n + 1)]
        for u, v, time in times:
            adjacency[u].append((v, time))
        
        times = [float("inf") for _ in range(n + 1)]
        times[k] = 0
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if time != times[node]:
                continue
            for nei, edgeTime in adjacency[node]:
                if time + edgeTime < times[nei]:
                    times[nei] = time + edgeTime
                    heapq.heappush(heap, (time + edgeTime, nei))
        
        maxTime = max(times[1:])
        if maxTime == float("inf"):
            return -1
        return maxTime