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

        # first pass to make the nodes
        hp = {None: None} # old node address : new node address

        curr = head
        while curr:
            hp[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        while curr:
            new_node = hp[curr]
            new_node.next = hp[curr.next]
            new_node.random = hp[curr.random]

            curr = curr.next

        # second pass to connect the next and random
        return hp[head]

        