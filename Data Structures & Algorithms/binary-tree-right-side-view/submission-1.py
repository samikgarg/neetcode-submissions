# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        currLevel = [0]
        def dfs(currNode, level):
            if currNode == None:
                return
            
            if level == currLevel[0]:
                res.append(currNode.val)
                currLevel[0] += 1
            
            dfs(currNode.right, level + 1)
            dfs(currNode.left, level + 1)
        
        dfs(root, 0)
        return res