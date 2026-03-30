class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # 9.39

        if not grid:
            return 0

        # multi source bfs starting from all rotten
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        time = 0
        fresh_count = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count +=1 

        if fresh_count == 0:
            return time 

        while q and fresh_count > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 0
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        fresh_count -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))

            time += 1

        return time if fresh_count == 0 else -1




