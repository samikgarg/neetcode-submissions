# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [0]
        finished = [False]
        visited = [0]
        def inorder(node):
            if not node or finished[0]:
                return
            inorder(node.left)
            visited[0] += 1
            if visited[0] == k:
                res[0] = node.val
                finished[0] = True
                return
            if visited[0] > k:
                return
            inorder(node.right)
            
        inorder(root)
        return res[0]
            
            

            