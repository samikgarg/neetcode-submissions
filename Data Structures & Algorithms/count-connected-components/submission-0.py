class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        notFound = set(range(n))
        
        adjacency = {i : [] for i in range(n)}
        for edge in edges:
            adjacency[edge[0]].append(edge[1])
            adjacency[edge[1]].append(edge[0])
        
        def dfs(node):
            if node not in notFound:
                return
            notFound.remove(node)
            for nextNode in adjacency[node]:
                dfs(nextNode)
        
        connectedComponents = 0
        while notFound:
            connectedComponents += 1
            dfs(next(iter(notFound)))
        
        return connectedComponents