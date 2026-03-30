class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != (n-1):
            return False

        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, parent):

            if node in visit:
                return False
            visit.add(node)
            for v in adj[node]:
                if v == parent:
                    continue
                if not dfs(v, node):
                    return False
            return True

        return dfs(0,-1) and len(visit) == n
        