class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        ####### SOLUTION 1 #####################
        def solution_1():
            # union find - O(V+E*a(V)) time and O(V) space
            n = len(edges)+1
            parent = [i for i in range(n)]
            rank = [0] * n

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
                if not union(u, v):
                    return [u,v]

            return []

        #return solution_1()
        
        ####### SOLUTION 2 #####################
        def solution_2():
            n = len(edges)+1
            adj = {i:[] for i in range(n)}
            indegree = [0] * (n)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
                indegree[u] += 1
                indegree[v] += 1

            # append all nodes with indegree = 1
            # cycle on node if indegree >= 2
            q = deque()
            for i in range(len(indegree)):
                if indegree[i] == 1:
                    q.append(i)

            while q:
                node = q.popleft()
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)

            for u, v in reversed(edges):
                if indegree[u] >= 2 and indegree[v] >= 2:
                    return [u,v]

            return []
        
        return solution_2()
