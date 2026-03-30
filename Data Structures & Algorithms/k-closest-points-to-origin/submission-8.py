class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []
        for point in points:
            x, y = point[0], point[1]
            dist = x*x + y*y
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k = k - 1

        return res
        



        