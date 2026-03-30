class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {i:[] for i in range(numCourses)}
        # directed graph
        for crs, prq in prerequisites:
            adj[crs].append(prq)

        visit = set() # track processed nodes
        cycle = set() # track current path
        res = []

        def dfs(node):
            if node in cycle:
                return False

            if node in visit:
                return True

            cycle.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res