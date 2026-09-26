class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distTo = [float("inf")] * n
        distTo[src] = 0

        for _ in range(k + 1):
            distToCopy = distTo[:]
            for fromNode, toNode, price in flights:
                distToCopy[toNode] = min(distToCopy[toNode], distTo[fromNode] + price)
            distTo = distToCopy
         
        if distTo[dst] == float("inf"):
            return -1
        return distTo[dst]