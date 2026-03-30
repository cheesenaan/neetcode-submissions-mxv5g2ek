class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # adj list
        adj_list = {i:[] for i in range(numCourses)}
        for crs, prq in prerequisites:
            adj_list[crs].append(prq)

        # dfs method
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

            visit.remove(crs)
            adj_list[crs] = []
            return True
            

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

        