class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # hp[points] = distance
        minHeap = []
        for x,y in points:
            d = x*x + y*y
            minHeap.append([d,x,y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            d,x,y= heapq.heappop(minHeap)
            res.append([x,y])
            k = k - 1

        return res




        