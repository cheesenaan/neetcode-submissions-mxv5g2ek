class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        for src, dest in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1

        q = deque()
        v = set()
        res = []
        finished = 0
        for crs in range(len(indegree)):
            if indegree[crs] == 0:
                q.append(crs)

        while q:
            crs = q.popleft()
            finished += 1
            res.append(crs)
            for prq in adj[crs]:
                indegree[prq] -= 1
                if indegree[prq] == 0:
                    q.append(prq)
        
        return res[::-1] if finished == numCourses else []

        