class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # max heap of size k
        maxHeap = []

        for x, y in points:
            dist = x*x + y*y

            # push negative distance to simulate max-heap
            heapq.heappush(maxHeap, (-dist, x, y))

            # keep heap size at k
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        # extract results
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])

        return res
