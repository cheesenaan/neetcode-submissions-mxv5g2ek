class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        if not edges:
            return []

        parent = [i for i in range(len(edges)+1)]
        rank = [0 for i in range(len(edges)+1)]

        # rec find parent of node
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # cycle found
            if p1 == p2:
                return False
            # join larger to smaller
            if rank[p1] < rank[p2]:
                parent[p2] = p1
            elif rank[p2] < rank[p1]:
                parent[p1] = p2
            else:
                parent[p1] = p2
                rank[p2] += 1
            return True

        
        for u,v in edges:
            if not union(u,v):
                return [u,v]
        
        return []

        