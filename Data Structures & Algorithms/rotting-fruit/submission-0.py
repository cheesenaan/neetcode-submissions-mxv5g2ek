class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        # bfs from each rotten fruit at the same time
        time = 0
        fresh_count = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return time

        while q and fresh_count > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        q.append((nr, nc))
                        fresh_count -= 1
                        grid[nr][nc] = 2

            time += 1

        return time if fresh_count == 0 else -1


        