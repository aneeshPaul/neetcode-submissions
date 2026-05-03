# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    import copy
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head and head.next:
            slow = head
            fast = head.next
        else:
            return

        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next

        prev= None
        curr = slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        
        left = head
        right = prev

        while right:
            temp1 = left.next
            left.next = right
            temp2 = right.next
            left = temp1
            right.next = left
            right = temp2
