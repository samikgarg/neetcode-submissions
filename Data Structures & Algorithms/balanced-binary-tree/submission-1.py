# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        isTreeBalanced = [True]

        def dfs(currNode):
            if not currNode or not isTreeBalanced[0]:
                return 0
            
            leftHeight = dfs(currNode.left)
            rightHeight = dfs(currNode.right)

            if abs(leftHeight - rightHeight) > 1:
                isTreeBalanced[0] = False
                return 0
            
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return isTreeBalanced[0]