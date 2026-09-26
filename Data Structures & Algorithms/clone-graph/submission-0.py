"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        created = {node : Node(node.val)}
        visited = set()
        def dfs(currNode):
            visited.add(currNode)
            for nextNode in currNode.neighbors:
                if nextNode not in created:
                    created[nextNode] = Node(nextNode.val)
                created[currNode].neighbors.append(created[nextNode])
                if nextNode not in visited:
                    dfs(nextNode)

        dfs(node)
        return created[node]