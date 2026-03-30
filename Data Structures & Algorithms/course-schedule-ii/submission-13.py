class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # time and space [ O(V+E)]
        # adj list
        adj = {i:[] for i in range(numCourses)}
        # number of edges coming to node
        indegree = [0] * numCourses
        # directed graph
        for src, dest in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1

        # append all indegree = 0 to q
        q = deque()
        finsihed = 0
        res = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            crs = q.popleft()
            indegree[crs] -= 1
            finsihed += 1
            res.append(crs)
            for prq in adj[crs]:
                indegree[prq] -= 1
                if indegree[prq] == 0:
                    q.append(prq)


        return res[::-1] if finsihed == numCourses else []

        