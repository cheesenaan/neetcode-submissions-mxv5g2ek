"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        hp = {} # old_node : new_node


        def dfs_recursive(node):
            if not node:
                return None

            if node in hp:
                return hp[node]

            copy_node = Node(node.val)
            hp[node] = copy_node
            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs_recursive(neighbor))

            return copy_node
            

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