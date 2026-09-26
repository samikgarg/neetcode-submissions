# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]
        def helper(node):
            if not node:
                return 0
            leftDiameter = helper(node.left)
            rightDiameter = helper(node.right)
            maxDiameter[0] = max(maxDiameter[0], leftDiameter + rightDiameter)
            return 1 + max(leftDiameter, rightDiameter)
        helper(root)
        return maxDiameter[0]