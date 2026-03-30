class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow points to head of second half 

        # reverse second half
        prev, curr = None, slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # prev contains reversed second half
        
        # merge
        first, second = head, prev

        while first and second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2

        
        if first:
            first.next = None

        return

        