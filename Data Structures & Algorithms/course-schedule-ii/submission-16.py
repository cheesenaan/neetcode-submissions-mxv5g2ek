class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {i:[] for i in range(numCourses)}
        # directed graph
        for crs, prq in prerequisites:
            adj[crs].append(prq)

        # dfs for cycle detection.
        # return false if cycle found
        visit = set() # track processed nodes
        cycle = set() # track current path
        res = []
        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True

            cycle.add(crs)
            for prq in adj[crs]:
                if not dfs(prq):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res

        

        