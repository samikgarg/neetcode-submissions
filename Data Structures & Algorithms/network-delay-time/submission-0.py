class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency = {i : [] for i in range(n)}
        for fromNode, toNode, time in times:
            adjacency[fromNode - 1].append((time, toNode - 1))
        
        notVisited = set(range(n))
        res = 0
        fringe = [(0, k - 1)]
        while notVisited and fringe:
            currDist, currNode = heapq.heappop(fringe)
            if currNode not in notVisited:
                continue
            notVisited.remove(currNode)
            for dist, adj in adjacency[currNode]:
                heapq.heappush(fringe, (dist + currDist, adj))
            res = max(res, currDist)
        if notVisited:
            return -1
        else:
            return res