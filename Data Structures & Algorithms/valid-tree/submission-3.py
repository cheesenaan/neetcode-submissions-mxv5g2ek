class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != (n-1):
            return False

        # adj list - undirected
        adj_list = {i:[] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # dfs cycle detection
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)
            for v in adj_list[node]:
                if v == parent:
                    continue 
                if not dfs(v, node):
                    return False
            return True

        def dfs_iterative(node, parent):
            
            stack = []
            stack.append([node, parent])

            while stack:
                node, parent = stack.pop()

                if node in visit:
                    return False

                visit.add(node)
                for v in adj_list[node]:
                    if v == parent:
                        continue 
                    stack.append([v, node])
            return True
        
        return dfs_iterative(0,-1) and len(visit) == n
        
        