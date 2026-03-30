class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]
        self.maxHeap = stones
        heapq.heapify(self.maxHeap)

        while len(self.maxHeap) > 1:
            # pop two max (heaviest stones)
            x, y = -heapq.heappop(self.maxHeap), -heapq.heappop(self.maxHeap)

            # both stones are destroyed
            if x != y:
                y = x-y
                heapq.heappush(self.maxHeap, -y)

        return -self.maxHeap[0] if self.maxHeap else 0
