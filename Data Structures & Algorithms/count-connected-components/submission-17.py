class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # union find - O(V+E*a(V)) time and O(V) space
        parent = [i for i in range(n)]
        rank = [0] * n
        components = n

        # recursively find parent
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        # return False if cycle else add edge to component
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
            if union(u, v):
                components -= 1

        return components

        