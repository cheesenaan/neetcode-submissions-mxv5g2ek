class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # n nodes -> n-1 edges
        # n nodes -> n edges
        n = len(edges)   
        adj = {i:[] for i in range(1, n+1)}
        for u, v in edges:
            print(u,v)
            adj[u].append(v) 
            adj[v].append(u) 

        def dfs(node):
            stack = []
            stack.append(node)
            visit.add(node)
            while stack:
                cur = stack.pop()
                for nei in adj[cur]:
                    if nei not in visit:
                        dfs(nei)
                        stack.append(nei)


        res = []
        for u, v in edges:
            # remove u -> v and v -> u from adj then re add after
            adj[u].remove(v) 
            adj[v].remove(u)

            # dfs : is not cycle ?
            visit = set()
            count = 0
            for node in range(1, n+1):
                if node not in visit:
                    dfs(node)
                    count+=1
            if count == 1:
                res.append([u,v])

            adj[u].append(v) 
            adj[v].append(u)

        return res[-1] if res else []

