# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def backtrack(root,path_sum):
            if not root:
                return False
            path_sum += int(root.val)

            if not root.left and not root.right:
                if path_sum == targetSum:
                    return True
                else:
                    return False
            if backtrack(root.left, path_sum):
                return True
            if backtrack(root.right, path_sum):
                return True
            path_sum-=root.val

            return False

        return backtrack(root , 0)
        