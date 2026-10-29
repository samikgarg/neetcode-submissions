# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = [-1]
        def dfs(currNode, numNodes):
            if not currNode or res[0] != -1:
                return numNodes
            
            currNodeNum = dfs(currNode.left, numNodes) + 1

            if currNodeNum == k:
                res[0] = currNode.val
                return float("inf")
            
            nextNodeNum = dfs(currNode.right, currNodeNum)

            return nextNodeNum
        
        dfs(root, 0)
        return res[0]