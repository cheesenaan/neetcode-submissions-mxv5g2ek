class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        # directed graph
        for crs, prq in prerequisites:
            adj[crs].append(prq)
            indegree[prq] += 1

        q = deque()
        finished = 0
        res = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            crs = q.popleft()
            finished += 1
            indegree[crs] -=1
            res.append(crs)
            for prq in adj[crs]:
                indegree[prq] -=1
                if indegree[prq] == 0:
                    q.append(prq)

        return res[::-1] if finished == numCourses else []



        