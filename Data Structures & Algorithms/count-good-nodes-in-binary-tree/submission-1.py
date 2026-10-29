# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        numGoodNodes = [0]

        def dfs(currNode, currMaxVal):
            if not currNode:
                return
            
            if currNode.val >= currMaxVal:
                numGoodNodes[0] += 1
            
            dfs(currNode.left, max(currMaxVal, currNode.val))
            dfs(currNode.right, max(currMaxVal, currNode.val))
        
        dfs(root, float("-inf"))
        return numGoodNodes[0]