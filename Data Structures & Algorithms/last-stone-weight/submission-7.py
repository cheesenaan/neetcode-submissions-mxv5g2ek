class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones] # o(n)
        heapq.heapify(maxHeap) # o(n)

        while len(maxHeap) > 1:
            x, y = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)

            if x != y:
                heapq.heappush(maxHeap, -(x-y))

        return -maxHeap[0] if maxHeap else 0

       
