class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        res = 0

        def dfs(node):
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)

        for node in range(n):
            if node not in visit:
                dfs(node)
                res+=1

        return res