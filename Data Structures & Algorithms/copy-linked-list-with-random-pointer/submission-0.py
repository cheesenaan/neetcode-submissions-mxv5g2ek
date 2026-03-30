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

        hp = {None:None} # old : new

        curr = head
        while curr:
            copy = Node(curr.val, None, None)
            hp[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = hp[curr]
            copy.next = hp[curr.next]
            copy.random = hp [curr.random]
            curr = curr.next

        return hp[head]

        

        