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
                return node

            if node in hp:
                return hp[node]

            hp[node] = Node(node.val)
            for neighbor in node.neighbors:
                hp[node].neighbors.append(dfs(neighbor))

            return hp[node]

        def dfs_iterative(node):

            if not node:
                return None

            stack = []
            stack.append(node)
            hp[node] = Node(node.val)

            while stack:
                cur = stack.pop()

                for neighbor in cur.neighbors:
                    if neighbor not in hp:
                        hp[neighbor] = Node(neighbor.val)
                        stack.append(neighbor)
                    hp[cur].neighbors.append(hp[neighbor])

            return hp[node]

        
        return dfs_iterative(node)

        

        