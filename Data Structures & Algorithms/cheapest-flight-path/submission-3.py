class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float('inf')] * n
        dist[src] = 0
        
        for i in range(k + 1):
            curr_dist = dist.copy()
            for from_flight, to_flight, price in flights:
                if dist[from_flight] + price < curr_dist[to_flight]:
                    curr_dist[to_flight] = dist[from_flight] + price
            dist = curr_dist
        
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]