class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyList = {course : [] for course in range(numCourses)}
        for prereq in prerequisites:
            adjacencyList[prereq[0]].append(prereq[1])
        
        unvisitedNodes = set(range(numCourses))
        currVisted = set()
        cache = {}
        def dfs(node):
            if node in cache:
                return cache[node]
            if node in currVisted:
                cache[node] = False
                return False
            unvisitedNodes.remove(node)
            currVisted.add(node)
            for nextNode in adjacencyList[node]:
                if not dfs(nextNode):
                    cache[node] = False
                    return False
            currVisted.remove(node)
            cache[node] = True
            return True
        
        while unvisitedNodes:
            currNode = unvisitedNodes.pop()
            unvisitedNodes.add(currNode)
            if not dfs(currNode):
                return False
        return True
