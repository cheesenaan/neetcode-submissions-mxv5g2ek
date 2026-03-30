class MedianFinder:

    def __init__(self):
        # store left half
        self.maxHeap = []
        # store right half
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        if self.maxHeap and num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if ((len(self.maxHeap) - len(self.minHeap)) > 1):
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        if ((len(self.minHeap) - len(self.maxHeap)) > 1):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        