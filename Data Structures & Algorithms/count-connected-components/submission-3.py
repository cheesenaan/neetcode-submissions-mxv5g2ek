class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        v = set()
        res = 0

        def dfs(node):
            stack = []
            stack.append(node)
            v.add(node)
            while stack:
                cur = stack.pop()
                for nei in adj[cur]:
                    if nei not in v:
                        dfs(nei)


        for node in range(n):
            if node not in v:
                res += 1
                dfs(node)

        return res


        