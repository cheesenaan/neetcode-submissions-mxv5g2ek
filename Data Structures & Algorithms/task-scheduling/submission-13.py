class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        # Maxheap (letter_count : time)
        # at each time take the max letter_count that is allowed 
        # after taking then time += n

        maxHeap = Counter(tasks)
        maxHeap = [-c for c in maxHeap.values()]
        q = deque()
        heapq.heapify(maxHeap)
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                letter_count = heapq.heappop(maxHeap) + 1
                if letter_count:
                    q.append([letter_count, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        
        return time
        

        