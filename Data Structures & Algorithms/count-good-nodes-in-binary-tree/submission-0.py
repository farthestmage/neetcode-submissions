# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node,highnode):
            nonlocal count
            if not node:
                return None
            if node.val>=highnode:
                count+=1
            highnode = max(node.val,highnode)

            dfs(node.left,highnode)
            dfs(node.right,highnode)
        dfs(root,root.val)
        return count