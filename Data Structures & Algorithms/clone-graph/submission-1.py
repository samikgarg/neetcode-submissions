"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        nodeMap = {}
        visited = set()

        num_printed = 0
        def dfs(curr_node):
            for nei in curr_node.neighbors:
                if nei not in nodeMap:
                    nodeMap[nei] = Node(nei.val)
                    dfs(nei)
                nodeMap[curr_node].neighbors.append(nodeMap[nei])
        
        nodeMap[node] = Node(node.val)
        dfs(node)
        return nodeMap[node]