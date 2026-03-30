class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # Build an array of (distance, x, y)
        # Time: O(n)
        # Space: O(n) for storing all points in the heap array
        minHeap = []
        for x, y in points:
            dist = x*x + y*y
            minHeap.append([dist, x, y])

        # Turn the array into a heap
        # Time: O(n)
        # Extra space: O(1) auxiliary (heapify is in-place)
        heapq.heapify(minHeap)

        res = []

        # Extract k smallest
        # Each pop: O(log n)
        # Total: O(k log n)
        # Extra space: O(1) per pop, but res grows to O(k)
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        # Overall time: O(n + k log n)
        # Overall space: O(n + k)
        return res
