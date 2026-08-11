# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = deque([p])
        queue_q = deque([q])


        while queue_p and queue_q:
            curr_p = queue_p.popleft()
            curr_q = queue_q.popleft()

            if not curr_p and not curr_q:
                continue
            
            if not curr_p or not curr_q or curr_p.val != curr_q.val:
                return False
            queue_p.append(curr_p.left)
            queue_p.append(curr_p.right)

            queue_q.append(curr_q.left)
            queue_q.append(curr_q.right)

        return True

            
        