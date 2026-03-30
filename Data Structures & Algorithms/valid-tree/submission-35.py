class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        
        if n-1 != len(edges):
            return False

        if not edges:
            return True

        adj = {i:[] for i in range(n)}
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque()
        count = 0
        for i in range(len(indegree)):
            if indegree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            count+=1
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)

        return count == n 

        