# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = [float('-inf')]
        def currMaxSum(node):
            if node is None:
                return float('-inf')
            leftSum = currMaxSum(node.left)
            rightSum = currMaxSum(node.right)
            MaxSumSoFar = max(node.val, leftSum + node.val, rightSum + node.val)
            maxSum[0] = max(maxSum[0], leftSum + rightSum + node.val, MaxSumSoFar)
            return max(0, MaxSumSoFar)
        currMaxSum(root)
        return maxSum[0]
