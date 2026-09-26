class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        wqu = DisjointSet(len(edges))
        for edge in edges:
            if wqu.isConnected(edge[0] - 1, edge[1] - 1):
                return edge
            else:
                wqu.connect(edge[0] - 1, edge[1] - 1)
        return []
        
class DisjointSet:
    def __init__(self, size):
        self.parent = [-1] * size
    
    def find(self, i):
        if self.parent[i] < 0:
            return i 
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def connect(self, a, b):
        p1 = self.find(a)
        p2 = self.find(b)
        if p1 == p2:
            return
        if self.parent[p1] < self.parent[p2]:
            self.parent[p1] += self.parent[p2]
            self.parent[p2] = p1
        else:
            self.parent[p2] += self.parent[p1]
            self.parent[p1] = p2
    
    def isConnected(self, a, b):
        return self.find(a) == self.find(b)
