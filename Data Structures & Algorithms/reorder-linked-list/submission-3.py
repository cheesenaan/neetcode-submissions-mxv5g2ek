# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        # split first and second
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

         # reverse second
        prev, curr = None, slow

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        first, second = head, prev

        # merge
        
        while first and second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2

        if first:
            first.next = None

        return

        