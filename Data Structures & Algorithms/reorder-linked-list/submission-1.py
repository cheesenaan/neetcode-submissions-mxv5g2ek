# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # first linked-list from n = [0, n/2]
        # second linked-list from n = [n/2, n]
        # reverse second linked-list
        # merge

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        prev, curr = None, slow

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        first, second = head, prev

        while first and second:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2

        if first:
            first.next = None

        return 

       



        

