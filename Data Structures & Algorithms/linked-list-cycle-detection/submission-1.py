# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = set()

        cur = head

        while cur:
            if cur.val in seen:
                return True
            seen.add(cur.val)
            cur = cur.next

        return False
            
        