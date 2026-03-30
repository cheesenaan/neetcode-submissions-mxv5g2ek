class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        
        parent = [i for i in range(n)] # parent is itself
        rank = [0] * n  # rank to find indegree of parent optimally
        components = n

        # return parent with path compression
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        # return boolean if n1, n2 can be union
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False 
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            parent[p2] = p1
            rank[p1] += rank[p2]
            return True

        for n1, n2 in edges:
            # union 
            if union(n1, n2):
                components -= 1

        return components



        

        