class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # tree property 
        if len(edges) != n - 1:
            return False

        
        # undirected graph
        adj_list = [[] for i in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        q = deque([(0, -1)])
        visited = set()
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for v in adj_list[node]:
                if v == parent:
                    continue 
                if v in visited:
                    return False
                visited.add(v)
                q.append([v, node])
                

        return len(visited) == n

        

