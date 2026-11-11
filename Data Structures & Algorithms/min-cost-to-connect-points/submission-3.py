import networkx as nx

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        points = [tuple(point) for point in points]

        edges = []
        for point1 in points:
            for point2 in points:
                if point1 != point2:
                    edges.append((
                        abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]), 
                        point1, 
                        point2
                    ))
        edges.sort()

        minCost = 0
        numEdges = 0
        uf = nx.utils.UnionFind(points)
        for cost, point1, point2 in edges:
            if numEdges == len(points) - 1:
                break
            if uf[point1] == uf[point2]:
                continue
            uf.union(point1, point2)
            minCost += cost
            numEdges += 1
        
        return minCost


        