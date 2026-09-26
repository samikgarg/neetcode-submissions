# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = [0]
        def helper(node, depth):
            if not node:
                maxDepth[0] = max(maxDepth[0], depth)
                return
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)
        helper(root, 0)
        return maxDepth[0]
            