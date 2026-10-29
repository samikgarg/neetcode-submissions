# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = [0]

        def dfs(currNode):
            if not currNode:
                return 0
            
            leftDepth = dfs(currNode.left)
            rightDepth = dfs(currNode.right)

            diameter[0] = max(diameter[0], leftDepth + 1 + rightDepth)

            return 1 + max(leftDepth, rightDepth)
        
        dfs(root)
        return diameter[0] - 1