class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        ####### SOLUTION 1 #####################
        def solution_1():
            # union find - O(V+E*a(V)) time and O(V) space
            parent = [i for i in range(n)]
            rank = [0] * n
            components = n

            # recursively find parent
            def find(node):
                if node != parent[node]:
                    parent[node] = find(parent[node])
                return parent[node]

            # return False if cycle else add edge to component
            def union(n1, n2):
                p1, p2 = find(n1), find(n2)
                if p1 == p2:
                    return False
                if rank[p1] < rank[p2]:
                    parent[p2] = p1
                elif rank[p1] > rank[p2]:
                    parent[p1] = p2
                else:
                    parent[p1] = p2
                    rank[p2] += 1
                return True

            for u, v in edges:
                if union(u, v):
                    components -= 1

            return components

        ####### SOLUTION 2 #####################
        def solution_2():
            # dfs - O(V+E) time and space
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

        return solution_2()