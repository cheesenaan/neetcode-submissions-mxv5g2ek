# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # add dummy node at beginning
        # start slow pointer at dummy, fast pointer at nth node starting from the left
        # move pointers while fast exists
        # move slow pointer to remove nth node

        dummy = ListNode(0, head)

        slow, fast = dummy, head

        for i in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

        