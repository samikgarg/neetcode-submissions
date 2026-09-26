class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distTo = [float("inf")] * len(points)
        distTo[0] = 0
        visited = [False] * len(points)
        edges = 0
        currPoint = 0
        cost = 0

        while edges < len(points) - 1:
            visited[currPoint] = True
            minDist = float("inf")
            minPoint = -1
            for i, point in enumerate(points):
                currDist = abs(points[currPoint][0] - point[0]) + abs(points[currPoint][1] - point[1])
                if currDist < distTo[i]:
                    distTo[i] = currDist
                if not visited[i] and distTo[i] < minDist:
                    minDist = distTo[i]
                    minPoint = i
            currPoint = minPoint
            edges += 1
            cost += distTo[currPoint]
        
        return cost

