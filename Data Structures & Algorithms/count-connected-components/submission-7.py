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
            if n1 == n2:
                return False
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False 
            min_node = min(p1, p2)
            max_node = max(p1, p2)
            # parent will be min_node
            rank[min_node] += 1
            parent[max_node] = min_node

            return True

        for n1, n2 in edges:
            # union 
            if union(n1, n2):
                components -= 1

        return components



        

        