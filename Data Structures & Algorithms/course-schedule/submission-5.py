class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjacency = [[] for _ in range(numCourses)]
        for after, before in prerequisites:
            adjacency[before].append(after)
        
        unvisited = list(range(numCourses))
        curr_visited = set()
        possible = [True]
        def dfs(curr_course):
            if not possible[0]:
                return
            
            curr_visited.add(curr_course)
            for nei in adjacency[curr_course]:
                if nei in curr_visited:
                    possible[0] = False
                    return
                if nei in unvisited:
                    unvisited.remove(nei)
                    dfs(nei)
            curr_visited.remove(curr_course)
        
        while unvisited:
            curr_course = next(iter(unvisited))
            unvisited.remove(curr_course)
            dfs(curr_course)
            if not possible[0]:
                return False
        
        return True