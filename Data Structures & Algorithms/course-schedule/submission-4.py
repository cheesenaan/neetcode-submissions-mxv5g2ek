class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # adj list -> course : [prepreq1, prereq2 ...]
        ajd_list = {i:[] for i in range(numCourses)}
        for crs, prq in prerequisites:
            ajd_list[crs].append(prq)

        visited = set()

        def dfs(crs):
            # cycle found
            if crs in visited:
                return False

            if ajd_list[crs] == []:
                return True

            visited.add(crs)

            for prq in ajd_list[crs]:
                if not dfs(prq):
                    return False

            visited.remove(crs)
            ajd_list[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True