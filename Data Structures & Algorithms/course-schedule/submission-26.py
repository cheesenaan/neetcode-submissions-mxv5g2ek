class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1 # increment destination

        q = deque()
        finsihed = 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            crs = q.popleft()
            indegree[crs] -= 1
            finsihed += 1
            for prq in adj[crs]:
                indegree[prq] -= 1
                if indegree[prq] == 0:
                    q.append(prq)

        return finsihed == numCourses
