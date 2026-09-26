# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        lst = []
        def preorder(node):
            if not node:
                lst.append(None)
                return
            lst.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return str(lst)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lst = eval(data)
        if not lst:
            return None
        def construct():
            curr_val = lst.pop(0)
            if curr_val is None:
                return None
            left_tree = construct()
            right_tree = construct()
            return TreeNode(curr_val, left_tree, right_tree)
        return construct()

