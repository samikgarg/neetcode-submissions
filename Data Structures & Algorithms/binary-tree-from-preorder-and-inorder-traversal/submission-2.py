# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        preorder_indices = {preorder[i] : i for i in range(len(preorder))}
        inorder_indices = {inorder[i] : i for i in range(len(inorder))}
        
        def helper(inorder_start, inorder_end, preorder_start, preorder_end):
            root = TreeNode(preorder[preorder_start])
            inorder_index = inorder_indices[root.val]

            if inorder_index == inorder_start:
                root.left = None
            else:
                next_preorder_end = preorder_start + (inorder_index - inorder_start)
                root.left = helper(inorder_start, inorder_index - 1, preorder_start + 1, next_preorder_end)
            
            if inorder_index == inorder_end:
                root.right = None
            else:
                next_preorder_start = preorder_end - (inorder_end - inorder_index) + 1
                root.right = helper(inorder_index + 1, inorder_end, next_preorder_start, preorder_end)
            
            return root
        
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

        