class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heapq.heappush(heap, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        
        edges = 0
        cost = 0
        wqu = WQU(len(points))
        while edges < len(points) - 1:
            currDist, i, j = heapq.heappop(heap)
            if wqu.isConnected(i, j):
                continue
            wqu.connect(i, j)
            edges += 1
            cost += currDist
        return cost

class WQU:
    def __init__(self, size):
        self.parent = [-1] * size
    
    def find(self, val):
        if self.parent[val] < 0:
            return val
        self.parent[val] = self.find(self.parent[val])
        return self.parent[val]
    
    def connect(self, val1, val2):
        parent1 = self.find(val1)
        parent2 = self.find(val2)
        if parent1 == parent2:
            return
        if self.parent[parent1] > self.parent[parent2]:
            parent1, parent2 = parent2, parent1
        self.parent[parent1] += self.parent[parent2]
        self.parent[parent2] = parent1
    
    def isConnected(self, val1, val2):
        return self.find(val1) == self.find(val2)
