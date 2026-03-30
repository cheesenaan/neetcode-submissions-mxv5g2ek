"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return 
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

        def dfs_iterative(node):

            stack = []
            stack.append(node)
            hp[node] = Node(node.val)
            while stack:
                cur = stack.pop()

                if cur is None:
                    return

                for nei in cur.neighbors:
                    if nei not in hp:
                        hp[nei] = Node(nei.val)
                        stack.append(nei)
                    hp[cur].neighbors.append(hp[nei])

            return hp[node]

        return dfs_iterative(node)



        