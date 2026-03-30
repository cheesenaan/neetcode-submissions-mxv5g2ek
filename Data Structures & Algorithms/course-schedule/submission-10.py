class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # indegree is number of edges coming to node
        indegree = [0] * numCourses
        adj_list = {i:[] for i in range(numCourses)}
        # src -> crs
        # dest -> prq
        for src, dest in prerequisites:
            indegree[dest] += 1
            adj_list[src].append(dest)

        finished = 0
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            crs = q.popleft()
            finished += 1
            for prq in adj_list[crs]:
                indegree[prq] -= 1
                if indegree[prq] == 0:
                    q.append(prq)
        
        return finished == numCourses

        