"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        hp = {} # old node : new node

        def dfs(node):

            if node in hp:
                return hp[node]

            new_node = Node(node.val)
            hp[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))

            return new_node

        return dfs(node) if node else None

        

        