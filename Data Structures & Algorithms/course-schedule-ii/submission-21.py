class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {i:[] for i in range(numCourses)}
        # directed graph
        indegree = [0] * numCourses
        for crs, prq in prerequisites:
            adj[crs].append(prq)
            indegree[prq] += 1

        q = deque()
        res = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        finished = 0
        while q:
            crs = q.popleft()
            finished += 1
            res.append(crs)
            for prq in adj[crs]:
                indegree[prq] -= 1
                if indegree[prq] == 0:
                    q.append(prq)

        return res[::-1] if finished == numCourses else []