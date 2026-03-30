class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # directed 
        adj_list = {i:[] for i in range(numCourses)}
        indegree = [0] * (numCourses)
        for u, v in prerequisites:
            adj_list[u].append(v)
            indegree[v] += 1

        q = deque()
        visit = set()
        res = []
        finished = 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            crs = q.popleft()
            indegree[crs] -= 1
            finished += 1
            res.append(crs)
            for prq in adj_list[crs]:
                indegree[prq] -= 1
                if indegree[prq] == 0:
                    visit.add(prq)
                    q.append(prq)

        return res[::-1] if finished == numCourses else []

        