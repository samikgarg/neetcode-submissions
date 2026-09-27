class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency = [[] for _ in range(n)]
        for src, dest, time in times:
            adjacency[src - 1].append((dest, time))
        
        times = [float('inf')] * n
        pq = []

        times[k - 1] = 0
        pq.append((0, k))

        while pq:
            time, node = heapq.heappop(pq)

            if time > times[node - 1]:
                continue

            for nei, edge_time in adjacency[node - 1]:
                if time + edge_time < times[nei - 1]:
                    heapq.heappush(pq, (time + edge_time, nei))
                    times[nei - 1] = time + edge_time
        
        max_time = max(times)
        if max_time == float('inf'):
            return -1
        else:
            return max_time