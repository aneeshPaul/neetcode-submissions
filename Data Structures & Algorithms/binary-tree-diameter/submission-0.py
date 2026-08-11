# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.dia = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return 0

            depth_l = dfs(root.left)
            depth_r = dfs(root.right)

            depth= 1 + max(depth_l,depth_r)
            self.dia = max(self.dia, depth_l + depth_r)

            return depth

        max_depth = dfs(root)

        return self.dia
        