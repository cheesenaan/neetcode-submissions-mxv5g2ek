class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # We want to schedule tasks so that the same task is separated by at least n intervals.
        # At each time unit, we should pick the task with the highest remaining frequency
        # that is currently allowed to run.

        # Count how many times each task appears
        maxHeap = Counter(tasks)

        # Convert counts to negative values so we can use Python's min-heap as a max-heap
        maxHeap = [-c for c in maxHeap.values()]

        # This queue will store tasks that are cooling down
        # Each entry is [remaining_count, time_when_task_can_run_again]
        q = deque()

        # Turn the list into a heap
        heapq.heapify(maxHeap)

        # This variable tracks the current time unit
        time = 0

        # Continue until there are no available tasks and no tasks in cooldown
        while maxHeap or q:

            # Move forward one unit of time
            time += 1

            # If there is an available task, schedule the one with the highest remaining count
            if maxHeap:
                # Pop the task with the largest remaining frequency
                # Add 1 because counts are stored as negative values
                letter_count = heapq.heappop(maxHeap) + 1

                # If this task still has remaining executions,
                # put it into the cooldown queue with the time it becomes available again
                if letter_count != 0:
                    q.append([letter_count, time + n])

            # If the task at the front of the cooldown queue is ready to be reused,
            # move it back into the heap so it can be scheduled again
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        # Once all tasks are scheduled, return the total time units used
        return time
