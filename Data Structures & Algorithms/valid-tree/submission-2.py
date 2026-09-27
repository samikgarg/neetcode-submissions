class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = [[] for _ in range(n)]
        for n1, n2 in edges:
            adjacency[n1].append(n2)
            adjacency[n2].append(n1)

        unvisited_nodes = set(range(n))
        def dfs(curr_node):
            for nei in adjacency[curr_node]:
                if nei in unvisited_nodes:
                    unvisited_nodes.remove(nei)
                    dfs(nei)
        
        unvisited_nodes.remove(0)
        dfs(0)

        if len(unvisited_nodes) > 0:
            return False
        return len(edges) == n - 1
            