class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        
        adj = {i:[] for i in range(len(edges)+1)}
        indegree = [0 for i in range(len(edges)+1)]
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 1:
                q.append(i)

        while q:
            cur = q.popleft()
            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)

        
        for u, v in reversed(edges):
            if indegree[u] >= 2 and indegree[v] >= 2:
                return [u,v]

        return []
        
        