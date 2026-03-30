class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        
        # dfs for cycle detection
        # if n-1 != len(edges):
        #     return False

        # adj = {i:[] for i in range(n)}
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        # visit = set()
        # def dfs(node, parent):
        #     if node in visit:
        #         return False

        #     visit.add(node)
        #     for nei in adj[node]:
        #         if nei == parent:
        #             continue
        #         if not dfs(nei, node):
        #             return False
        #     return True

        # return dfs(0, -1) and len(visit) == n

        # bfs for cycle detection indegree
        if n-1 != len(edges):
            return False

        if n == 1:
            return True
        
        adj = {i:[] for i in range(n)}
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 1:
                q.append(i)

        finished = 0
        while q:
            cur = q.popleft()
            finished += 1
            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        
        return finished == n


        # union-find then return components == 1

        
        