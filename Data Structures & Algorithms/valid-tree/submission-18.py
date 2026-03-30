class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        
        if n-1 != len(edges):
            return False
            
        parent = [i for i in range(n)]
        rank = [0] * n
        components = n

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
            elif rank[p2] < rank[p1]:
                parent[p1] = p2
            else:
                parent[p1] = p2
                rank[p2] += 1
            return True

        for u,v in (edges):
            if union(u, v):
                components -= 1

        return components == 1

        

        