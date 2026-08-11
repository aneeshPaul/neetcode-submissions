# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.balance_flag = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0

            if not self.balance_flag:
                return 0

            depth_l = dfs(root.left)
            depth_r = dfs(root.right)

            if abs(depth_l - depth_r) > 1:
                self.balance_flag = False

            return 1 + max(depth_l,depth_r)

        max_depth = dfs(root)

        return self.balance_flag

            

        