# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        isValid = [True]

        def dfs(currNode, minVal, maxVal):
            if not currNode or not isValid[0]:
                return
            
            if not(minVal < currNode.val < maxVal):
                isValid[0] = False
                return
            
            dfs(currNode.left, minVal, currNode.val)
            dfs(currNode.right, currNode.val, maxVal)
        
        dfs(root, float("-inf"), float("inf"))
        return isValid[0]