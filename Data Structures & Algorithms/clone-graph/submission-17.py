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
            if not node:
                return 
            
            if node in hp:
                return hp[node]

            hp[node] = Node(node.val)

            for nei in node.neighbors:
                hp[node].neighbors.append(dfs(nei))

            return hp[node]

        return dfs(node)



        