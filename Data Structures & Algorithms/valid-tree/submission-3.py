class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [-1] * n

        def find(node):
            if parents[node] < 0:
                return node
            parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            if parent1 == parent2:
                return
            if parents[parent1] < parents[parent2]:
                parents[parent1] += parents[parent2]
                parents[parent2] = parent1
            else:
                parents[parent2] += parents[parent1]
                parents[parent1] = parent2
        
        def is_connected(node1, node2):
            return find(node1) == find(node2)
        
        for node1, node2 in edges:
            if is_connected(node1, node2):
                return False
            union(node1, node2)
        
        num_parents = 0
        for parent in parents:
            if parent < 0:
                num_parents += 1
        return num_parents == 1
