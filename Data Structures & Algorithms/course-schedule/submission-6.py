class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj_list = {i:[] for i in range(numCourses)}
        for crs, prq in prerequisites:
            adj_list[crs].append(prq)

        v = set()
        def dfs(crs):
            if crs in v:
                return False

            if adj_list[crs] == []:
                return True

            v.add(crs)
            for prq in adj_list[crs]:
                if not dfs(prq):
                    return False
            v.remove(crs)
            adj_list[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True

        