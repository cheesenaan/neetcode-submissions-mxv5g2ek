class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {i:[] for i in range(numCourses)}
        for crs, prq in prerequisites:
            adj[crs].append(prq)

        v = set() # track all processed nodes
        c = set() # track nodes in current path
        res = []
        
        def dfs(crs):
            if crs in c:
                return False

            if crs in v:
                return True

            c.add(crs)
            for prq in adj[crs]:
                if not dfs(prq):
                    return False
            c.remove(crs)
            v.add(crs)
            res.append(crs)
            adj[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res
