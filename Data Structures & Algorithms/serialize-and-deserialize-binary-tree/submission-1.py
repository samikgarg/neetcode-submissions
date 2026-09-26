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
        def construct(index):
            if lst[index] is None:
                return (index, None)
            left_index, left_tree = construct(index + 1)
            right_index, right_tree = construct(left_index + 1)
            return (right_index, TreeNode(lst[index], left_tree, right_tree))
        return construct(0)[1]

