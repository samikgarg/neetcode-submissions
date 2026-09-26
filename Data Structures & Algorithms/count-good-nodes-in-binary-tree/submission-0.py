# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def maxVal(node, maxSoFar):
            if not node:
                return
            if maxSoFar <= node.val:
                res[0] += 1
            maxSoFar = max(node.val, maxSoFar)
            maxVal(node.left, maxSoFar)
            maxVal(node.right, maxSoFar)
        maxVal(root, root.val)
        return res[0]
            