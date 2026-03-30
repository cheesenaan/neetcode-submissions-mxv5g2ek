class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # bfs method

        # adj_list
        indegree = [0] * numCourses
        adj_list = {i:[] for i in range(numCourses)}
        for src, dest in prerequisites:
            indegree[dest] += 1
            adj_list[src].append(dest)

        finished = 0
        res = []
        q = deque()

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            crs = q.popleft()
            finished += 1
            res.append(crs)
            for prq in adj_list[crs]:
                indegree[prq] -= 1
                if indegree[prq] == 0:
                    q.append(prq)

        return res[::-1] if finished == numCourses else []