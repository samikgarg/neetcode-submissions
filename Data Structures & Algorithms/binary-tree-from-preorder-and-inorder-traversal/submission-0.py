# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        for i, n in enumerate(inorder):
            indices[n] = i
        queue = deque(preorder)
        
        def construct(start, end):
            if start > end:
                return None
            if start == end:
                queue.popleft()
                return TreeNode(inorder[start])
            currVal = queue.popleft()
            index = indices[currVal]
            left = construct(start, index - 1)
            right = construct(index + 1, end)
            return TreeNode(currVal, left, right)

        return construct(0, len(inorder) - 1)
            
            