class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = {course : [] for course in range(numCourses)}
        for prereq in prerequisites:
            adjacencyList[prereq[0]].append(prereq[1])

        res = []
        currVisited = set()
        notAdded = set(range(numCourses))
        possible = [True]
        def dfs(course):
            if not possible[0]:
                return 
            if course in currVisited:
               possible[0] = False
               return
            currVisited.add(course)
            for nextCourse in adjacencyList[course]:
                dfs(nextCourse)
            if course in notAdded:
                res.append(course)
                notAdded.remove(course)
            currVisited.remove(course)
        
        while notAdded:
            dfs(next(iter(notAdded)))
            if not possible[0]:
                return []
        
        return res
        