class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) #o(n)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # o(nlogn)
        
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # o(nlogn)

        return self.minHeap[0]

       