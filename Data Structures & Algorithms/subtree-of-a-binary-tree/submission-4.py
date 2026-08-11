# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        sub = False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.sub = False

        def isSame(p,q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSame(p.left, q.left) and isSame(p.right, q.right)
            else:
                return False

        def dfs(root, subRoot):
            if not root and not subRoot:
                return
            elif not root:
                return
            elif not subRoot:
                return
            elif root.val == subRoot.val:
                self.sub = isSame(root, subRoot)
                if self.sub:
                    return
            dfs(root.left, subRoot)
            dfs(root.right, subRoot)

        dfs(root, subRoot)

        return self.sub


        