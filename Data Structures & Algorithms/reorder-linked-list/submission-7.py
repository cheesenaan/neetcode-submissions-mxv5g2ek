class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # first half [0:n/2]
        # second half [n/2 : n]
        # reverse second half
        # merge them

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # prev contains reversed linked list of second half

        # merge
        first, second = head, prev
        while first and second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2

        if first:
            first.next = None

        return 






        