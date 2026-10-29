# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # RIght side vieww ???
        
        res = []
        def rdfs(node,depth = 0):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)
            
            rdfs(node.right,depth+1)
            rdfs(node.left,depth+1)
           
        rdfs(root)
        return res