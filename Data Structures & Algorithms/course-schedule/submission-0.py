class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adj list to map courses to pre-reqs
        adj_list = {i:[] for i in range(numCourses)}

        for crs, prq in prerequisites:
            adj_list[crs].append(prq)

        print(adj_list)

        visited = set()

        # dfs function 
        def dfs(crs):
            if crs in visited:
                return False

            if adj_list[crs] == []:
                return True

            visited.add(crs)
            for prq in adj_list[crs]:
                if not dfs(prq):
                    return False
            visited.remove(crs)
            adj_list[crs] = []
            return True
            

        # dfs on every course
        for crs in adj_list:
            if not dfs(crs):
                return False

        return True
        