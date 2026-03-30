class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        time = 0
        count = Counter(tasks) #o(n)
        maxHeap = [-cnt for cnt in count.values()] #o(n)
        heapq.heapify(maxHeap) #o(n)
        q = deque()

        while q or maxHeap:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time+n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time

