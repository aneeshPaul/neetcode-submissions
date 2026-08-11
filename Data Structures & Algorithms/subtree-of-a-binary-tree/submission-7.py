# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(p,q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSame(p.left, q.left) and isSame(p.right, q.right)
            
            return False

        def dfs(root, subRoot):
            if not subRoot:
                return True
            if not root:
                return False
            if isSame(root, subRoot):
                return True
            return dfs(root.left, subRoot) or dfs(root.right,subRoot)

        return dfs(root, subRoot)


        