class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i:[] for i in range(numCourses)}
        for crs, prq in prerequisites:
            adj[crs].append(prq)

        v = set()
        def dfs(crs):
            if crs in v:
                return False

            if adj[crs] == []:
                return True

            v.add(crs)
            for prq in adj[crs]:
                if not dfs(prq):
                    return False
            v.remove(crs)
            adj[crs] == []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

        