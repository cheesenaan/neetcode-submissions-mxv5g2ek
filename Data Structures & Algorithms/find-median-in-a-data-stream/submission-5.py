class MedianFinder:

    def __init__(self):
        # store first half
        self.maxHeap = []
        # store second half
        self.minHeap = []
        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)
        

    def addNum(self, num: int) -> None:
        if self.maxHeap and num > -self.maxHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
            

        # balance
        if len(self.maxHeap) > len(self.minHeap) and ((len(self.maxHeap) - len(self.minHeap)) > 1):
            max_val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, max_val)

        if len(self.minHeap) > len(self.maxHeap) and ((len(self.minHeap) - len(self.maxHeap)) > 1):
            min_val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -min_val)

        return

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
                return -self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2


