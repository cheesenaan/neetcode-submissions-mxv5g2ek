class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        p = [i for i in range(n)]
        r = [0] * n
        c = n

        def find(node):
            if node != p[node]:
                p[node] = find(p[node])
            return p[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # cycle
            if p1 == p2:
                return False

            if r[p1] < r[p2]:
                p[p2] = p1
            elif r[p2] < r[p1]:
                p[p1] = p2
            else:
                p[p1] = p2
                r[p2] += 1
            return True

        
        for u, v in edges:
            if union(u,v):
                c -= 1

        return c

        