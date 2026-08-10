# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def find_depth(root, max_depth):
            if not root:
                return 0

            # left_depth = find_depth(root.left, max_depth)
            # right_depth = find_depth(root.right, max_depth)
            
            return 1 + max(find_depth(root.left, max_depth), find_depth(root.right, max_depth))

        return find_depth(root, 0)


        