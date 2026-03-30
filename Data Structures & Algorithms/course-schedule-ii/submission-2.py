class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = {i:[] for i in range(numCourses)}
        for crs, prq in prerequisites:
            adj_list[crs].append(prq)

        visit = set() # track all processed nodes
        cycle = set() # track current path
        res = [] 

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True

            cycle.add(crs)
            for prq in adj_list[crs]:
                if not dfs(prq):
                    return False
            
            adj_list[crs] = []
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res

        