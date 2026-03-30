class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            adj_list[u].append(v)

        # dfs for cycle detection
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False

            if adj_list[crs] == []:
                return True

            visit.add(crs)
            for prq in adj_list[crs]:
                if not dfs(prq):
                    return False
            adj_list[crs] = []
            visit.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

        