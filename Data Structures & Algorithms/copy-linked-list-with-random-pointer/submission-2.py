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
        hp = {None : None} # old to new node addresses

        # first pass to create the nodes
        curr = head
        while curr:
            hp[curr] = Node(curr.val, None, None)
            curr = curr.next

        # second to make the links
        
        curr = head
        while curr:
            copy = hp[curr]
            copy.next = hp[curr.next]
            copy.random = hp[curr.random]
            curr = curr.next

        return hp[head]