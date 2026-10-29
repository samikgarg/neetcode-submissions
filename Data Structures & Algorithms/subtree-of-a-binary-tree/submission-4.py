# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p, q):
        if not p or not q:
            return not p and not q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False
        
        if root.val == subRoot.val:
            return (self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

