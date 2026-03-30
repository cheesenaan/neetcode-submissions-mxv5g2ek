class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # number of edges coming to node
        indegree = [0] * numCourses
        adj_list = {i:[] for i in range(numCourses)}
        # src -> crs
        # prq -> dest
        for src, dest in prerequisites:
            adj_list[src].append(dest)
            indegree[dest] += 1

        # add all courses where indegree = 0 to q
        q = deque()
        finished = 0
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        # bfs on q
        while q:
            crs = q.popleft()
            finished += 1
            for prq in adj_list[crs]:
                # decrement indegree
                indegree[prq] -= 1
                if indegree[prq] == 0:
                    q.append(prq)



        return finished == numCourses

        


        