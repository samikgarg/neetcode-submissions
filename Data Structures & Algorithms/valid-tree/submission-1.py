class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Rule: Connected and E = V - 1

        #Check if E = V - 1
        if len(edges) != n - 1:
            return False

        #Check if fully connected
        #Perform DFS from arbitrary node to see if all nodes can be reached 
        adjacencyList = {i : [] for i in range(n)}
        for edge in edges:
            adjacencyList[edge[0]].append(edge[1])
            adjacencyList[edge[1]].append(edge[0])
        
        notFound = set(range(n))
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            if node in notFound:
                notFound.remove(node)   
            for nextNode in adjacencyList[node]:
                dfs(nextNode)
        
        dfs(0)
        if notFound:
            return False
        return True
            