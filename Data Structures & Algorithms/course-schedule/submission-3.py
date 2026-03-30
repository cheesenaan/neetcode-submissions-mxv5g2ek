class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # adj list -> course : [prepreq1, prereq2 ...]
        adj_list = {i:[] for i in range(numCourses)}
        for element in prerequisites:
            crs, prq = element[0], element[1]
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
             

        # dfs cycle detection

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
        