# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # issue is fast A - find the sub root for that we have to traverse the tree

        def checkSameTree(node1,node2):
            if not node1 and not node2:
                return True
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            left = checkSameTree(node1.left,node2.left)
            right = checkSameTree(node1.right,node2.right)

            return (left and right)
        # find subroot use BFS for this ??
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
            # ??
        q = deque ([root])
        boox = False
        while q:
            node = q.popleft()
            if node.val  == subRoot.val:
                boox = checkSameTree(node,subRoot)
            if boox:
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return boox

