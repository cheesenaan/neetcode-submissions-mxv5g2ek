class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # adj list
        adj_list = {i:[] for i in range(numCourses)}
        for crs, prq in prerequisites:
            adj_list[crs].append(prq)

        v = set() # tracks fully processed nodes
        cycles = set() # tracks current path
        res = []
        def dfs(crs):

            if crs in cycles:
                return False

            if crs in v:
                return True

            cycles.add(crs)

            for prq in adj_list[crs]:
                if not dfs(prq):
                    return False

            v.add(crs)
            cycles.remove(crs)
            res.append(crs)
            adj_list[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res

        


        