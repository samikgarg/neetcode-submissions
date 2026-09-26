# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        def helper(node):
            if node is None:
                return 0
            left_height = helper(node.left)
            right_height = helper(node.right)
            if abs(left_height - right_height) > 1:
                balanced[0] = False
            return 1 + max(left_height, right_height)
        helper(root)
        return balanced[0]
            