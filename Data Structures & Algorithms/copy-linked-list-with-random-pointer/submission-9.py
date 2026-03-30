"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # two pass
        hp = {None : None} #old node : new node

        curr = head
        while curr:
            hp[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        while curr:
            hp[curr].next = hp[curr.next]
            hp[curr].random = hp[curr.random]
            curr = curr.next

        return hp[head]




