class KthLargest:

    # time  : O(m * logk) where m = number of times add is called 
    # space : O(k) 
    
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # o(n)

        # ensure self.minHeap is max length = k
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # o(logn)

        return

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # o(logn)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # o(logn)

        return self.minHeap[0]


        
