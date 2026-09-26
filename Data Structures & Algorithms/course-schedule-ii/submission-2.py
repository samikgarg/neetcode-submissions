class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency = [[] for _ in range(numCourses)]
        for after, before in prerequisites:
            adjacency[before].append(after)
        
        reverse_topological = []
        unvisited = set(range(numCourses))
        possible = [True]

        curr_visited = set()
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
            reverse_topological.append(curr_course)
            curr_visited.remove(curr_course)
        
        while unvisited:
            curr_course = next(iter(unvisited))
            unvisited.remove(curr_course)
            dfs(curr_course)
            if not possible[0]:
                return []
        
        return reverse_topological[::-1]

            