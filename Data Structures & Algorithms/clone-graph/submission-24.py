"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        hp = {}
        def dfs(node):
            if not node:
                return

            if node in hp:
                return hp[node]

            new_node = Node(node.val)
            hp[node] = new_node
            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))

            return hp[node]

        return dfs(node)


        