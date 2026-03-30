# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # linked list with [0 : n/2]
        # linked list with [n/2 : n]
        # reverse [n/2 : n] list
        # merge


        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow contains second half of linked list [n/2 : n]

        # reverse [n/2 : n]
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # prev is the reversed linked list
        

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

        