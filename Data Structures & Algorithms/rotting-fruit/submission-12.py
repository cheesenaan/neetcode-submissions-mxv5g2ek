class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        time = 0

        # count fresh fruit - 1
        # multi source bfs from rotten fruit - 2
        q = deque()
        fresh_count = 0
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))

        if fresh_count == 0:
            return time

        while q and fresh_count > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                visit.add((r,c))
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visit
                    ): 
                        fresh_count -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        visit.add((nr, nc))

            time += 1

        return time if fresh_count == 0 else -1


        