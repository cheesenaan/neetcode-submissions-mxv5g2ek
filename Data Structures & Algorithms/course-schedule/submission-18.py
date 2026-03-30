class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # adj list
        adj = {i:[] for i in range(numCourses)}
        # directed graph
        for crs, prq in prerequisites:
            adj[crs].append(prq)

        visit = set() # track visited nodes
        # dfs for cycle detection
        def dfs(crs):
            if crs in visit:
                return False

            if adj[crs] == []:
                return True

            visit.add(crs)
            for prq in adj[crs]:
                if not dfs(prq):
                    return False
            visit.remove(crs)
            adj[crs] == []
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

        