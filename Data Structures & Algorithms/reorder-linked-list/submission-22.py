class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # head of second half
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is pointer to second half
        # head is pointer to first half

        # reverse the second half
        prev, cur = None, slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # prev contains head to reversed second half
        # head contains head to first half
        first, second = head, prev
        while first and second:
            f2 = first.next
            s2 = second.next
            first.next = second
            second.next = f2
            first, second = f2, s2

        if first:
            first.next = None

        return 

        