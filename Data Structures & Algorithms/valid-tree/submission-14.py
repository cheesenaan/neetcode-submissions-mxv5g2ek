class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n-1 != len(edges):
            return False

        adj = {i:[] for i in range(n)}
        degree = [0] * (n)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # dfs for cycle detection
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        return dfs(0,-1) and len(visit) == n