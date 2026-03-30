class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # djistras - bfs with minHeap
        adj = {i:[] for i in range(1,n+1)}
        for u,v,t in times:
            adj[u].append((t,v))

        t = 0
        minHeap = [(0, k)]
        visit = set()
        while minHeap:
            t1, v1 = heapq.heappop(minHeap)

            if v1 in visit:
                continue 

            t = max(t, t1)
            visit.add(v1)

            for t2, v2 in adj[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (t1+t2, v2))


        return t if len(visit) == n else -1


        