class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [0] * (n+1)

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] < rank[p2]:
                parent[p2] = p1
            elif rank[p1] > rank[p2]:
                parent[p1] = p2
            else:
                parent[p1] = p2
                rank[p2] += 1
            return True

        for u, v in edges:
            if not union(u,v):
                return [u,v]

        return []
        
        