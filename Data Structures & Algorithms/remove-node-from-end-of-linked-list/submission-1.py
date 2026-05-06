# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head
        i = 0

        while cur:
            i+=1
            cur= cur.next

        n = i - n
        if n == 0:
            return head.next

        i= 0
        cur = head
        while i < n-1:
            i+=1
            cur= cur.next

        if cur.next:
            cur.next = cur.next.next

        return head
        