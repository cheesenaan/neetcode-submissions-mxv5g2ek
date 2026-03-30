class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

            # keep only k largest elements in the heap
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        # root of the min-heap is the k-th largest element
        return minHeap[0]
